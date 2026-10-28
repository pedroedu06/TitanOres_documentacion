# Farming

Solarite, Emberite and Titanium can be **grown**, Mystical Agriculture style: plant the seeds on **Blue Soil**, harvest
essence and turn it into nuggets.

## Blue Soil

![](assets/icons/blue_soil.png){ .mc-inline } `titanores:blue_soil`

The only block the essence crops grow on (not farmland or grass). Its recipe is added by the modpack (KubeJS).
Mine it with a shovel.

## Crops

| Seeds | Crop | Harvest (mature) |
|---|---|---|
| ![](assets/icons/solarite_seed.png){ .mc-inline } Solarite Seeds | `titanores:solarite_crop` | 1 ![](assets/icons/solarite_essence.png){ .mc-inline } Solarite Essence + 1 seed back (+25% chance of an extra seed) |
| ![](assets/icons/emberite_seed.png){ .mc-inline } Emberite Seeds | `titanores:emberite_crop` | 1 ![](assets/icons/emberite_essence.png){ .mc-inline } Emberite Essence + 1 seed back (+25% chance of an extra seed) |
| ![](assets/icons/titanium_seed.png){ .mc-inline } Titanium Seeds | `titanores:titanium_crop` | 1 ![](assets/icons/titanium_essence.png){ .mc-inline } Titanium Essence + 1 seed back (+25% chance of an extra seed) |

- Crops have 8 growth stages and need light, like wheat, but grow **slower** (about 45 minutes on average).
- Breaking an unripe crop only gives the seed back.
- **Bone meal does not work.** Special growth items and accelerators from other mods (for example Mystical
  Agriculture's Fertilized Essence and Growth Accelerators) do.

## Essence to nuggets

8 essences in a ring on a crafting table make **1 nugget**.

<div class="recipes">
--8<-- "recipes/solarite_nugget_from_essence.html"
--8<-- "recipes/emberite_nugget_from_essence.html"
--8<-- "recipes/titanium_nugget_from_essence.html"
</div>

!!! note "Credits"
    The crop growth textures come from [Mystical Agriculture](https://github.com/BlakeBr0/MysticalAgriculture) by
    BlakeBr0 (MIT License), recolored for each ore.
