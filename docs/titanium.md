# Titanium

<div class="hero-icons" markdown>
![Titanium Ore](assets/icons/titanium_ore.png)
![Titanium Ingot](assets/icons/titanium_ingot.png)
![Titanium Nugget](assets/icons/titanium_nugget.png)
![Titanium Dust](assets/icons/titanium_dust.png)
![Block of Titanium](assets/icons/titanium_block.png)
</div>

The endgame ore. Its ore and ingot are animated.

## Where & How

| Property | Value |
|---|---|
| Dimension | The End |
| Biome | End Highlands (outer islands) |
| Height | Y 16 – 56 |
| Vein size | up to 3 blocks |
| Frequency | 2 attempts per chunk (like ancient debris) |
| Replaces | end stone |
| Exposure | never touches air: dig inside the islands |
| Pickaxe needed | **Emberite pickaxe** (level 6) or better |

!!! tip
    Use `/locatebiome minecraft:end_highlands` after reaching the outer islands.

!!! info "Mine it yourself"
    - **No automation:** quarries, digital miners and builders (any fake player) cannot break this ore, and if a machine breaks it anyway it drops nothing.
    - **Explosion proof:** TNT and creepers cannot destroy the ore or its storage block (blast resistance 1200).
    - **Fire resistant:** every TitanOres item survives lava and fire.

## Processing

Smelt the ore to get an ingot (the blast furnace is twice as fast).

<div class="recipes">
--8<-- "recipes/titanium_ingot_from_smelting.html"
--8<-- "recipes/titanium_ingot_from_blasting.html"
</div>

## Storage

<div class="recipes">
--8<-- "recipes/titanium_block.html"
--8<-- "recipes/titanium_ingot_from_block.html"
--8<-- "recipes/titanium_nugget.html"
--8<-- "recipes/titanium_ingot_from_nuggets.html"
</div>

## Titanium Star

The upgrade material for the final gear tier. See [Special Items](items.md#titanium-star).

<div class="recipes">
--8<-- "recipes/titanium_star.html"
</div>

## Items

| Item | ID | Notes |
|---|---|---|
| ![](assets/icons/titanium_ore.png){ .mc-inline } Titanium Ore | `titanores:titanium_ore` | drops itself |
| ![](assets/icons/titanium_ingot.png){ .mc-inline } Titanium Ingot | `titanores:titanium_ingot` | tag `forge:ingots/titanium` |
| ![](assets/icons/titanium_nugget.png){ .mc-inline } Titanium Nugget | `titanores:titanium_nugget` | tag `forge:nuggets/titanium` |
| ![](assets/icons/titanium_dust.png){ .mc-inline } Titanium Dust | `titanores:titanium_dust` | tag `forge:dusts/titanium` (no recipe yet, for ore processing mods) |
| ![](assets/icons/titanium_block.png){ .mc-inline } Block of Titanium | `titanores:titanium_block` | needs the same pickaxe as the ore |
