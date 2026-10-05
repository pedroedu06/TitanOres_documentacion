# Titan Factory

![](assets/icons/titan_factory.png){ .mc-inline } `titanores:titan_factory`

An energy-powered machine that combines two columns of items into one result.

!!! warning "Work in progress"
    The name may change and more recipes are coming.

## Crafting

<div class="recipes">
--8<-- "recipes/titan_factory.html"
</div>

| Symbol | Ingredient |
|---|---|
| Emberite Ingot / Solarite Ingot | from this mod |
| Glass | any colorless glass (`#forge:glass/colorless`) |
| Iron Gear | any mod's iron gear (`#forge:gears/iron`): Thermal Foundation, Immersive Engineering, ... |
| Machine Block | any block in `#titanores:machine_blocks` |

The `titanores:machine_blocks` tag ships with optional entries (ignored when the mod is missing): Mekanism Steel
Casing, Thermal Machine Frame, Industrial Foregoing Machine Frame, Immersive Engineering Light Engineering Block and
RFTools Machine Frame. Modpacks can add more with a datapack (`data/titanores/tags/items/machine_blocks.json` with
`"replace": false`) or KubeJS.

## How it works

- Put the ingredients in the **two columns** (3 slots on the left, 3 on the right, top to bottom).
- When the items match a recipe and the output has room, the machine starts working and spends energy **gradually**
  (total recipe energy ÷ recipe time, every tick).
- If the energy runs out, it **pauses** and resumes when power comes back (progress is kept).
- Removing the ingredients resets the progress.
- The bar under the output shows the progress; hover the red bar on the right to see the stored energy.

## Energy

| Property | Value |
|---|---|
| Energy type | Forge Energy (FE / RF): works with Mekanism, Powah, Thermal, etc. |
| Buffer | **100,000,000 FE** |
| Input limit | none (limited only by the cable) |
| Accepts energy from | every side |

## Speed upgrades

![](assets/icons/speed_upgrade.png){ .mc-inline } **Speed Upgrade** (`titanores:speed_upgrade`) goes into the
**upgrade slot** in the tab on the right side of the GUI, next to the energy bar (up to 4 stacked). Hover the tab icon to see how many are installed.

| Upgrades | Speed | Emberium recipe time | FE/t |
|---|---|---|---|
| 0 | x1 | 60 s | ~33,333 |
| 1 | x2 | 30 s | ~66,667 |
| 2 | x4 | 15 s | ~133,334 |
| 3 | x8 | 7.5 s | ~266,667 |
| 4 | x16 | 3.75 s | ~533,334 |

Each upgrade halves the recipe time. The **total energy per craft stays the same**, so the machine pulls more FE per
tick: faster crafting needs better cables and generators. It is made in the machine itself (see Recipes below).

## Automation

| Side | Items |
|---|---|
| **Top** | **Input.** Hoppers, pipes, AE2 / Refined Storage interfaces insert here. |
| **Bottom** | **Output.** Pull the result from below. |
| Sides | no item access |

Upgrade slots are not accessible by automation.

!!! tip "Smart column filling"
    Recipes are column based, so items inserted from the top go to the column that already holds the same item
    (or the first empty column) and are spread over its 3 slots. Inserting 3 Emberite Ingots and then
    3 Titanium Ingots from a hopper builds the Emberium recipe automatically.

## Recipes

<div class="recipes">
--8<-- "recipes/emberium_ingot_from_titan_factory.html"
--8<-- "recipes/emberium_block_from_titan_factory.html"
--8<-- "recipes/speed_upgrade_from_titan_factory.html"
--8<-- "recipes/titan_crafter_from_titan_factory.html"
</div>

The Speed Upgrade needs the plain **Potion of Swiftness** (3:00): the long, strong and splash versions are not accepted.
Its columns mix different items, so it has to be filled by hand (top automation cannot build it).

!!! tip "JEI"
    With JEI installed, press **U** on the Titan Factory (or **R** on a result) to see its recipes drawn on the machine
    GUI, with the energy each one needs and an animated progress bar. In the machine GUI, click the arrows to open
    them, and use JEI's **+** button to move the ingredients from your inventory into the right columns.

## Recipe format (modpacks)

Recipes are data-driven (`data/<namespace>/recipes/*.json`) and can be added or changed with a datapack:

```json
{
  "type": "titanores:titan_factory",
  "left":  [ {"item": "titanores:emberite_ingot"}, {"item": "titanores:emberite_ingot"}, {"item": "titanores:emberite_ingot"} ],
  "right": [ {"item": "titanores:titanium_ingot"}, {"item": "titanores:titanium_ingot"}, {"item": "titanores:titanium_ingot"} ],
  "mirrored": true,
  "energy": 40000000,
  "time": 1200,
  "result": { "item": "titanores:emberium_ingot", "count": 3 }
}
```

| Field | Meaning |
|---|---|
| `left`, `right` | Up to 3 ingredients each, top to bottom. `null` = that slot must be empty. Each position consumes 1 item. Tags work (`{"tag": "forge:ingots/iron"}`). |
| `mirrored` | Also accept the two columns swapped. |
| `energy` | Total FE for one craft. |
| `time` | Ticks (20 ticks = 1 second). FE per tick = `energy / time`. |
| `result` | Output item and count. |
