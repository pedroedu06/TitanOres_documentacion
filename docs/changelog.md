# Changelog

## 1.0.5

- The **final items** (Source Crystal, Sponge Bob, Ancestral Seed, World Core, Raid King, Antenna, Calculator, Iron Man
  Mask, Titanium Music Disc, Universal Remote) and **Blue Soil** moved to **Titan Utilities** (ids `titanutilities:*`).
  Essence crops now grow on the `#titanores:essence_crop_soil` block tag (Titan Utilities adds Blue Soil).

## 1.0.4

- The **Hephaestus Forge Upgrades** moved to **Titan Utilities** (`titanutilities:forge_upgrade_tier_2..5`).
- Titan Crafter recipe (Titan Utilities): the iron blocks were replaced by **Enderium Blocks**.

## 1.0.3

- New companion mod **Titan Utilities** (required by the TitanMods modpack). The **Titan Factory**, **Titan Crafter**
  and **Speed Upgrade** moved there, with their recipes and JEI categories (ids `titanutilities:*`, machine block tag
  `#titanutilities:machine_blocks`).
- Package renamed to `com.titanmods.titanores`.

## 1.0.2

- **Hephaestus Forge Upgrades** (Tier II, III, IV, X): right-click a Forbidden & Arcanus Hephaestus Forge to raise its tier.

## 1.0.1

- **Ore processing:** 2x in any crusher (Mekanism, IE, Create, Occultism, Blood Magic) and up to 5x with Mekanism (clumps, shards, crystals, dirty dust, slurries); dust smelts into ingots.
- **Farming:** Blue Soil and Solarite, Emberite and Titanium crops (seeds, essences, 25% extra seed chance, 8 essences → 1 nugget; slower than wheat, no bone meal).

## 1.0.0

- **Ores:** Solarite (deep oceans), Emberite (Warped Forest) and Titanium (End Highlands), with manual-mining protection. The ore items show where to find them (dimension, biome and Y range).
- **Emberium alloy:** made in the Titan Factory (3 Emberite + 3 Titanium Ingots → 3 Emberium, 40M FE; or 3 + 3 blocks → 3 Emberium Blocks, 80M FE).
- **Tools:** Solarite, Emberite, Titanium (Area Mode, tree felling, fire aspect, auto-smelt) and Titanium Star.
- **Armor:** Solarite, Emberite, Titanium and Titanium Star (90% damage reduction, flight, night vision), with per-piece abilities and a custom armor bar.
- **Special items:** Titanium Heart, Solarite Apple, Solarite Carrot, Solarite Lantern, Solarite Magnet and Titanium Star.
- **Titan Factory** machine: 100M FE buffer, gradual energy use, top input / bottom output automation, data-driven `titanores:titan_factory` recipes, upgrade slot for up to 4 Speed Upgrades (each doubles the speed). Crafting recipe for the machine (iron gears and machine blocks from any mod, via tags). Speed Upgrade recipe: 2 Clocks + 2 Potions of Swiftness + 2 Solarite Ingots, 800k FE.
- **Titan Crafter** machine: 9×7 fixed-position shaped crafting (`titanores:titan_crafting`), 200M FE buffer, template-style top input, made in the Titan Factory.
- **Titanium Music Disc** recipe in the Titan Crafter (36 Titanium Ingots + any music disc, 36M FE).
- **JEI:** Titan Factory recipe category and Titan Crafter recipe categories (machine GUI, energy needed, animated progress, + button to fill the machine).
- **Final items:** Source Crystal, Sponge Bob, Ancestral Seed, World Core, Raid King, Antenna, Calculator, Iron Man Mask, Titanium Music Disc and Universal Remote (the modpack's endgame components; recipes via KubeJS).
- `/titanores hearts` command, Curios and Mantle integration.
