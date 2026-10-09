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

## Final items

Endgame components of the Titan Modpack (about 10 are planned). They have **no recipe in the mod**: the modpack adds
their recipes with KubeJS.

| Item | Id |
|---|---|
| ![](assets/icons/source_crystal.png){ .mc-inline } Source Crystal | `titanores:source_crystal` |
| ![](assets/icons/sponge_bob.png){ .mc-inline } Sponge Bob | `titanores:sponge_bob` (made with Create in the modpack) |
