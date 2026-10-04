# Architecture

Root package: `com.titanmodpack.titanores` · mod id `titanores`.

## Packages

| Package | Contents |
|---|---|
| `init` | All registries (`DeferredRegister`): blocks, items, tile entities, containers, recipe serializers, loot modifiers, tags and the creative tab |
| `block` | Custom blocks and tile entities: manual-mining ore, lantern and invisible light, Titan Factory |
| `item` | Tool tiers (`ModItemTier`), armor materials (`ModArmorMaterial`), custom items and the Area Mode helper |
| `event` | Forge event handlers: armor abilities, automation blocker, mob spawns and dragon drop, health, tools, magnet |
| `world` | Ore generation (`ModOreGeneration`) |
| `loot` | Global loot modifiers (`auto_smelt`, `replace_with_item`) |
| `recipe` | `titanores:upgrade_shaped` (keeps the NBT of the upgraded armor piece) and `titanores:titan_factory` (machine recipes) |
| `energy` | `ModEnergyStorage`, the Forge Energy buffer used by machines |
| `network` | `SimpleChannel` and the Night Vision toggle packet |
| `client` | Client-only code: screens, keybinds and HUD (armor bar, compact health bar) |
| `container` | Titan Factory container |
| `compat` | Optional Curios integration (only loaded when Curios is present) |
| `command` | `/titanores` commands |

## Key systems

- **Worldgen:** configured features are registered in `FMLCommonSetupEvent` and added per biome in
  `BiomeLoadingEvent`. Emberite and Titanium use `NO_SURFACE_ORE`, like ancient debris.
- **Manual mining:** `ManualMiningOreBlock` returns no drops unless a real player breaks it, and `AutomationBlocker`
  cancels the `BreakEvent` of fake players for blocks in `titanores:manual_mining_only`.
- **Tiers:** tool stats live in `ModItemTier` and armor stats in `ModArmorMaterial`. Unbreakable tiers use 0
  durability and override `isEnchantable`.
- **Titanium tools:** `AreaToolHelper` handles the Area Mode NBT flag, the toggle and the 3×3 breaking through
  `ServerPlayerEntity.gameMode.destroyBlock` (respects protections and normal drops), with a recursion guard.
- **Titan Factory:** `TitanFactoryTileEntity` (tickable) holds a 7-slot `ItemStackHandler` and a `ModEnergyStorage`
  (100M FE, receive-only). Item capability per side: top = `TitanFactoryItemHandlers.TopInput` (column-aware insert),
  bottom = `BottomOutput`, sides = none; energy on every side. Recipes: `recipe/TitanFactoryRecipe`, type
  `titanores:titan_factory`. GUI data is synced through an `IIntArray` (energy split into two 16-bit halves).

## Conventions

- Everything is in **English**: ids, file names and code comments. Portuguese only in `lang/pt_br.json`.
- Textures live in lowercase per-material folders: `textures/item/<material>/<material>_<item>.png` and
  `textures/block/<material>/`. Worn armor goes in `textures/models/armor/`, interfaces in `textures/gui/`.
- Every item is fire resistant (`ModItems.props()`).
