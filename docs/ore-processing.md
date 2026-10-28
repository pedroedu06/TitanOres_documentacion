# Ore Processing

Solarite, Emberite and Titanium ores can be multiplied like regular metals. Every route ends in **dust**, which smelts
into an ingot (furnace or blast furnace).

## 2x: any crusher

One ore gives **2 dusts** in:

- Mekanism **Enrichment Chamber**
- Immersive Engineering **Crusher**
- Create **Crushing Wheels** and **Millstone**
- Occultism **crusher spirit**
- Blood Magic **ARC** (with cutting fluid)

These recipes only load when the mod is installed.

## Mekanism: up to 5x

| Output | Route |
|---|---|
| **2x** | Enrichment Chamber: ore → 2 dust |
| **3x** | Purification Chamber (oxygen): ore → 3 clumps → Crusher → dirty dust → Enrichment Chamber → dust |
| **4x** | Chemical Injection Chamber (hydrogen chloride): ore → 4 shards → Purification Chamber → clump → … |
| **5x** | Chemical Dissolution Chamber (sulfuric acid): ore → 1000 mB dirty slurry → Chemical Washer (water) → clean slurry → Chemical Crystallizer (200 mB) → crystal → Chemical Injection Chamber → shard → … |

Mekanism stops at 5x (there is no 6x tier in Mekanism for 1.16).

## Intermediate items

| Ore | Dirty dust | Clump | Shard | Crystal | Slurries |
|---|---|---|---|---|---|
| Solarite | ![](assets/icons/solarite_dirty_dust.png){ .mc-inline } | ![](assets/icons/solarite_clump.png){ .mc-inline } | ![](assets/icons/solarite_shard.png){ .mc-inline } | ![](assets/icons/solarite_crystal.png){ .mc-inline } | `titanores:dirty_solarite`, `titanores:clean_solarite` |
| Emberite | ![](assets/icons/emberite_dirty_dust.png){ .mc-inline } | ![](assets/icons/emberite_clump.png){ .mc-inline } | ![](assets/icons/emberite_shard.png){ .mc-inline } | ![](assets/icons/emberite_crystal.png){ .mc-inline } | `titanores:dirty_emberite`, `titanores:clean_emberite` |
| Titanium | ![](assets/icons/titanium_dirty_dust.png){ .mc-inline } | ![](assets/icons/titanium_clump.png){ .mc-inline } | ![](assets/icons/titanium_shard.png){ .mc-inline } | ![](assets/icons/titanium_crystal.png){ .mc-inline } | `titanores:dirty_titanium`, `titanores:clean_titanium` |

Item tags follow Mekanism's names (`mekanism:clumps/<ore>`, `mekanism:shards/<ore>`, `mekanism:crystals/<ore>`,
`mekanism:dirty_dusts/<ore>`), so other mods and KubeJS scripts can use them.
