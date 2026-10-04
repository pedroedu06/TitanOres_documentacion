"""Sync data from the TitanOres mod into the docs.

- Copies item/block icons (first frame of animated textures) to docs/assets/icons/<item_id>.png
- Generates one HTML snippet per recipe in docs/snippets/recipes/<recipe_name>.html

Usage (from the docs repo root):
    python scripts/sync_from_mod.py [path/to/TitanOres]
Default mod path: ../TitanOres
"""
import html
import io
import json
import re
import struct
import sys
import zlib
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
MOD = Path(sys.argv[1]) if len(sys.argv) > 1 else DOCS.parent / "TitanOres"
RES = MOD / "src" / "main" / "resources"
ASSETS = RES / "assets" / "titanores"
RECIPES = RES / "data" / "titanores" / "recipes"
ICONS_OUT = DOCS / "docs" / "assets" / "icons"
SNIPPETS_OUT = DOCS / "docs" / "snippets" / "recipes"

LANG = json.loads((ASSETS / "lang" / "en_us.json").read_text(encoding="utf-8"))


# ---------- PNG helpers (no external dependencies) ----------

def read_png(path):
    data = path.read_bytes()
    pos, idat = 8, b""
    while pos < len(data):
        length, = struct.unpack(">I", data[pos:pos + 4])
        kind = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, depth, color = struct.unpack(">IIBB", chunk[:10])
            if depth != 8 or color != 6:
                return None  # only RGBA8 textures are handled; others are copied as-is
        elif kind == b"IDAT":
            idat += chunk
    raw = zlib.decompress(idat)
    stride = width * 4
    rows, prev, i = [], bytearray(stride), 0
    for _ in range(height):
        filt = raw[i]
        line = bytearray(raw[i + 1:i + 1 + stride])
        i += 1 + stride
        for x in range(stride):
            a = line[x - 4] if x >= 4 else 0
            b = prev[x]
            c = prev[x - 4] if x >= 4 else 0
            if filt == 1:
                line[x] = (line[x] + a) & 255
            elif filt == 2:
                line[x] = (line[x] + b) & 255
            elif filt == 3:
                line[x] = (line[x] + (a + b) // 2) & 255
            elif filt == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line)
        prev = line
    return width, height, rows


def write_png(path, width, rows):
    raw = b"".join(b"\x00" + bytes(r) for r in rows)

    def chunk(kind, payload):
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)

    path.write_bytes(b"\x89PNG\r\n\x1a\n"
                     + chunk(b"IHDR", struct.pack(">IIBBBBB", width, len(rows), 8, 6, 0, 0, 0))
                     + chunk(b"IDAT", zlib.compress(raw))
                     + chunk(b"IEND", b""))


# ---------- icons ----------

def texture_for_item(item_id):
    """Resolve the texture an item shows in the inventory."""
    model = json.loads((ASSETS / "models" / "item" / f"{item_id}.json").read_text(encoding="utf-8"))
    textures = model.get("textures", {})
    if "layer0" in textures:
        return textures["layer0"]
    parent = model.get("parent", "")
    if parent.startswith("titanores:block/"):
        block = json.loads((ASSETS / "models" / "block" / (parent.split("/", 1)[1] + ".json")).read_text(encoding="utf-8"))
        bt = block.get("textures", {})
        for key in ("all", "north", "front", "side", "particle"):
            if key in bt:
                return bt[key]
    return None


def block_faces(item_id):
    """Top/left/right textures for cube block items, or None for non-cube models."""
    model = json.loads((ASSETS / "models" / "item" / f"{item_id}.json").read_text(encoding="utf-8"))
    parent = model.get("parent", "")
    if not parent.startswith("titanores:block/"):
        return None
    block = json.loads((ASSETS / "models" / "block" / (parent.split("/", 1)[1] + ".json")).read_text(encoding="utf-8"))
    t = block.get("textures", {})
    if block.get("parent") == "minecraft:block/cube_all" and "all" in t:
        return t["all"], t["all"], t["all"]
    if block.get("parent") == "minecraft:block/cube" and "up" in t:
        return t["up"], t.get("north", t["up"]), t.get("east", t["up"])
    return None


def load_frame(texture):
    """First frame of a texture as rows of RGBA pixels, or None if it cannot be read."""
    png = read_png(ASSETS / "textures" / (texture.split(":", 1)[1] + ".png"))
    if not png:
        return None
    width, _, rows = png
    return width, [[tuple(r[i:i + 4]) for i in range(0, width * 4, 4)] for r in rows[:width]]


def render_iso(top, left, right, size=64):
    """Isometric cube like the inventory view: lit top, darker left and right faces."""
    half, quarter = size // 2, size // 4
    out = [[(0, 0, 0, 0)] * size for _ in range(size)]

    def sample(face, u, v, shade):
        w, px = face
        if not (0 <= u < 1 and 0 <= v < 1):
            return None
        r, g, b, a = px[int(v * w)][int(u * w)]
        return (int(r * shade), int(g * shade), int(b * shade), a)

    for y in range(size):
        for x in range(size):
            fx, fy = x + 0.5, y + 0.5
            # top: origin (0, q), u -> (half, -q), v -> (half, +q)
            a, b = fx / half, (fy - quarter) / quarter
            c = sample(top, (a - b) / 2, (a + b) / 2, 1.0)
            if c is None and fx < half:
                u = fx / half
                c = sample(left, u, (fy - quarter - quarter * u) / half, 0.8)
            if c is None and fx >= half:
                u = (fx - half) / half
                c = sample(right, u, (fy - half + quarter * u) / half, 0.62)
            if c and c[3]:
                out[y][x] = c
    return [bytes(v for p in row for v in p) for row in out]


def copy_icons():
    ICONS_OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for model_file in sorted((ASSETS / "models" / "item").glob("*.json")):
        item_id = model_file.stem
        texture = texture_for_item(item_id)
        if not texture:
            continue
        src = ASSETS / "textures" / (texture.split(":", 1)[1] + ".png")
        if not src.exists():
            print(f"  missing texture for {item_id}: {src}")
            continue
        dst = ICONS_OUT / f"{item_id}.png"
        faces = block_faces(item_id)
        frames = [load_frame(t) for t in faces] if faces else None
        if frames and all(frames):
            write_png(dst, 64, render_iso(*frames))
            count += 1
            continue
        png = read_png(src)
        if png and png[1] > png[0]:  # animated strip: keep the first frame
            width, _, rows = png
            write_png(dst, width, rows[:width])
        else:
            dst.write_bytes(src.read_bytes())
        count += 1
    print(f"icons: {count}")


# ---------- recipes ----------

def item_name(item_id):
    ns, path = item_id.split(":", 1)
    if ns == "titanores":
        return LANG.get(f"item.titanores.{path}") or LANG.get(f"block.titanores.{path}") or path
    return path.replace("_", " ").title()


TAG_NAMES = {
    "forge:gears/iron": "Iron Gear",
    "forge:glass/colorless": "Glass",
    "titanores:machine_blocks": "Machine Block",
}


def tag_slot(tag):
    """Tag ingredients (any mod): readable label plus '(any)', the tag id in the tooltip."""
    name = TAG_NAMES.get(tag) or tag.split(":", 1)[1].split("/")[-1].replace("_", " ").title()
    label = html.escape(f"{name} (any)")
    return f'<span class="mc-slot" title="{html.escape("#" + tag)}"><span class="mc-label">{label}</span></span>'


def slot(ingredient, count=1):
    if not ingredient:
        return '<span class="mc-slot"></span>'
    if isinstance(ingredient, dict) and "tag" in ingredient:
        return tag_slot(ingredient["tag"])
    item_id = ingredient["item"] if isinstance(ingredient, dict) else ingredient
    name = item_name(item_id)
    potion = re.search(r'Potion:"?(?:minecraft:)?([a-z_]+)', ingredient.get("nbt", "")) if isinstance(ingredient, dict) else None
    if potion:
        name = f"{name} of {potion.group(1).replace('_', ' ').title()}"
    name = html.escape(name)
    ns, path = item_id.split(":", 1)
    badge = f'<span class="mc-count">{count}</span>' if count > 1 else ""
    if ns == "titanores" and (ICONS_OUT / f"{path}.png").exists():
        inner = f'<img src="../assets/icons/{path}.png" alt="{name}">'
    else:
        # Vanilla/other mods: no textures are copied, show a short label instead.
        inner = f'<span class="mc-label">{name}</span>'
    return f'<span class="mc-slot" title="{name}">{inner}{badge}</span>'


def result_of(recipe):
    res = recipe["result"]
    if isinstance(res, str):
        return res, 1
    return res["item"], res.get("count", 1)


def render(recipe):
    kind = recipe["type"]
    out_id, out_count = result_of(recipe)
    result = slot(out_id, out_count)
    if kind in ("minecraft:crafting_shaped", "titanores:upgrade_shaped"):
        pattern = recipe["pattern"]
        key = recipe["key"]
        cells = []
        for r in range(3):
            row = pattern[r] if r < len(pattern) else ""
            for c in range(3):
                ch = row[c] if c < len(row) else " "
                cells.append(slot(key.get(ch)) if ch != " " else slot(None))
        label = "Crafting Table" + (" · keeps enchantments" if kind == "titanores:upgrade_shaped" else "")
        return grid(cells, result, label)
    if kind == "minecraft:crafting_shapeless":
        ings = recipe["ingredients"]
        cells = [slot(ings[i]) if i < len(ings) else slot(None) for i in range(9)]
        return grid(cells, result, "Crafting Table (shapeless)")
    if kind in ("minecraft:smelting", "minecraft:blasting"):
        station = "Furnace" if kind == "minecraft:smelting" else "Blast Furnace"
        seconds = recipe.get("cookingtime", 200) / 20
        return line([slot(recipe["ingredient"])], result, f"{station} · {seconds:g}s · {recipe.get('experience', 0)} XP")
    if kind == "titanores:titan_factory":
        left = (recipe.get("left") or []) + [None] * 3
        right = (recipe.get("right") or []) + [None] * 3
        cells = []
        for r in range(3):
            cells += [slot(left[r]), '<span class="mc-gap"></span>', slot(right[r])]
        seconds = recipe.get("time", 200) / 20
        label = f"Titan Factory · {recipe['energy']:,} FE · {seconds:g}s"
        if recipe.get("mirrored"):
            label += " · columns can be swapped"
        return grid(cells, result, label)
    if kind == "minecraft:smithing":
        return line([slot(recipe["base"]), '<span class="mc-op">+</span>', slot(recipe["addition"])], result,
                    "Smithing Table · keeps enchantments")
    return f"<p><em>Unsupported recipe type {html.escape(kind)}</em></p>"


def grid(cells, result, label):
    return (f'<div class="mc-recipe"><div class="mc-grid">{"".join(cells)}</div>'
            f'<span class="mc-arrow">&#10140;</span>{result}<div class="mc-station">{label}</div></div>\n')


def line(parts, result, label):
    return (f'<div class="mc-recipe"><div class="mc-line">{"".join(parts)}</div>'
            f'<span class="mc-arrow">&#10140;</span>{result}<div class="mc-station">{label}</div></div>\n')


def generate_recipes():
    SNIPPETS_OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for recipe_file in sorted(RECIPES.glob("*.json")):
        recipe = json.loads(recipe_file.read_text(encoding="utf-8"))
        (SNIPPETS_OUT / f"{recipe_file.stem}.html").write_text(render(recipe), encoding="utf-8")
        count += 1
    print(f"recipes: {count}")


if __name__ == "__main__":
    print(f"mod: {MOD}")
    copy_icons()
    generate_recipes()
