# Modpack Integration

## Forge tags

Every material registers the usual Forge tags, so ore processing mods and recipes in the pack recognise them.

| Tag | Values |
|---|---|
| `forge:ores/<material>` | Solarite, Emberite, Titanium ores (items and blocks) |
| `forge:ingots/<material>` | Solarite, Emberite, Titanium, Emberium |
| `forge:nuggets/<material>` | Solarite, Emberite, Titanium |
| `forge:dusts/<material>` | Solarite, Emberite, Titanium, Emberium |
| `forge:storage_blocks/<material>` | all material blocks |
| `forge:rods/solarite` | Solarite Stick |

!!! note "Dusts"
    The dusts have no recipe in the mod. They exist for ore processing recipes added by the pack (for example with KubeJS or CraftTweaker).

## Manual mining tag

`titanores:manual_mining_only` (block tag) contains the three ores. For blocks in this tag:

- fake players (quarries, digital miners, builders) cannot break them, because the break event is cancelled;
- the ores themselves drop nothing when broken by anything other than a real player.

The tag can be extended with a datapack to protect blocks from other mods.

## Data-driven content

Everything below can be changed with datapacks or KubeJS, without touching the code:

| What | Where |
|---|---|
| Recipes | `data/titanores/recipes/` (types: vanilla, `minecraft:smithing`, `titanores:upgrade_shaped`) |
| Block drops | `data/titanores/loot_tables/blocks/` |
| Piglin bartering apple | global loot modifier `titanores:solarite_apple_from_bartering` (1% chance) |
| Auto-smelt of Titanium tools | global loot modifier `titanores:auto_smelt` (smelts items in `forge:ores`) |

## Optional mods

| Mod | Integration |
|---|---|
| **Curios API** | The Solarite Magnet works in the charm slot |
| **Mantle** | When installed, TitanOres turns off its own compact health bar and lets Mantle draw the colored hearts |
| **JEI** | Shows every recipe (recommended) |
