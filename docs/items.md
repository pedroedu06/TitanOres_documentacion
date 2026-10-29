# Special Items

## Titanium Heart

![](assets/icons/titanium_heart.png){ .mc-inline } `titanores:titanium_heart`

- **Source:** dropped by the **Ender Dragon** every time it dies. In the End it appears on top of the exit portal pillar, so it never falls into the void.
- **Effect:** eat it to gain **+2 max hearts permanently**. It can be eaten any time and as many times as you want (Minecraft caps max health at 1024).
- The extra hearts are **kept after death** and after leaving the world.
- Admins can manage them with [`/titanores hearts`](commands.md).

## Solarite Apple

![](assets/icons/solarite_apple.png){ .mc-inline } `titanores:solarite_apple`

- **Source:** **Piglin bartering only**. Each gold trade has a **1%** chance to give a Solarite Apple instead of the normal loot. There is no crafting recipe.
- **Effects (3 minutes):** Health Boost V (+10 hearts), Absorption V (+10 hearts), Fire Resistance, Resistance, Night Vision, Regeneration II.

## Solarite Carrot

![](assets/icons/solarite_carrot.png){ .mc-inline } `titanores:solarite_carrot`

- Can only be eaten when hungry.
- **Effects:** Saturation for **8 minutes** (the hunger bar stays full) and Regeneration for **10 minutes**.

<div class="recipes">
--8<-- "recipes/solarite_carrot.html"
</div>

## Solarite Lantern

![](assets/icons/solarite_lantern.png){ .mc-inline } `titanores:solarite_lantern`

- **Lights up the area:** slowly places invisible light sources in dark spots within **16 blocks** (max 128 lights). They are removed when the lantern is broken.
- **No hostile spawns:** natural hostile mob spawning is blocked in the **3×3 chunks** around it. Spawners and spawn eggs still work.
- Needs an **iron pickaxe** or better. With **Silk Touch** it drops itself; otherwise it drops **8 Solarite Nuggets**.

<div class="recipes">
--8<-- "recipes/solarite_lantern.html"
</div>

## Solarite Magnet

![](assets/icons/solarite_magnet.png){ .mc-inline } `titanores:solarite_magnet`

- **Right-click in the air** to turn it on or off (`Magnet: ON/OFF` above the hotbar). It glows while on.
- While on, it pulls dropped **items and XP orbs** within **11 blocks**, from anywhere in your inventory.
- Works in a **Curios charm slot** when Curios API is installed.
- Respects the `PreventRemoteMovement` flag used by other mods (for example, items on conveyors).

<div class="recipes">
--8<-- "recipes/solarite_magnet.html"
</div>

## Titanium Star

![](assets/icons/titanium_star.png){ .mc-inline } `titanores:titanium_star`

The upgrade material for the [Titanium Star tools](tools.md) and [armor](armor.md). Each upgrade consumes one star
(40 Titanium Ingots + 1 Nether Star).

<div class="recipes">
--8<-- "recipes/titanium_star.html"
</div>

## Hephaestus Forge Upgrades

For **Forbidden & Arcanus**: in the 1.16 version the Hephaestus Forge has tiers but no way to upgrade them. These
items do it: **right-click the forge** with the next tier's upgrade (a tier 1 forge needs Tier II, and so on).

| Item | Id | Forge tier |
|---|---|---|
| ![](assets/icons/forge_upgrade_tier_2.png){ .mc-inline } Forge Upgrade (Tier II) | `titanores:forge_upgrade_tier_2` | 1 → 2 |
| ![](assets/icons/forge_upgrade_tier_3.png){ .mc-inline } Forge Upgrade (Tier III) | `titanores:forge_upgrade_tier_3` | 2 → 3 |
| ![](assets/icons/forge_upgrade_tier_4.png){ .mc-inline } Forge Upgrade (Tier IV) | `titanores:forge_upgrade_tier_4` | 3 → 4 |
| ![](assets/icons/forge_upgrade_tier_5.png){ .mc-inline } Forge Upgrade (Tier X) | `titanores:forge_upgrade_tier_5` | 4 → X |

In the Titan Modpack they are made with Hephaestus Forge rituals adapted from Forbidden & Arcanus 1.21.1 (each ritual
fits the essence limits of the forge's current tier; the 1.16 forge has only 6 pedestals):

| Upgrade | Forge item | Pedestals | Aureal / Souls / Blood |
|---|---|---|---|
| Tier II | Edelwood Planks | 3 Arcane Crystal, 3 Spawner Scrap | 200 / 1 / 5,000 |
| Tier III | Chiseled Polished Darkstone | 3 Arcane Crystal, 3 Arcane Gold Ingot | 500 / 5 / 9,000 |
| Tier IV | Chiseled Polished Darkstone | 3 Stellarite Piece, 3 Rune | 800 / 10 / 12,000 |
| Tier X | Stellarite Block | 2 Nether Star, 2 Dark Nether Star, 2 Dragon Scale | 1,000 / 100 / 20,000 |
