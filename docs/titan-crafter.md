# Titan Crafter

![](assets/icons/titan_crafter.png){ .mc-inline } `titanores:titan_crafter`

An energy-powered **9×6 crafting grid** for the mod's final crafts. Recipes are shaped with **fixed positions**: every
item has to be in its exact slot.

!!! warning "Work in progress"
    The final recipes are not defined yet.

## Crafting

Made in the [Titan Factory](titan-factory.md):

<div class="recipes">
--8<-- "recipes/titan_crafter_from_titan_factory.html"
</div>

The iron gears are temporary: the plan is to use diamond gears once the modpack has them.

## How it works

- Place the items in the grid exactly as the recipe shows (JEI page or **+** button).
- When the grid matches a recipe and the output has room, the machine spends energy **gradually**
  (recipe energy ÷ recipe time, every tick) and pauses without power, keeping its progress.
- Each used slot consumes 1 item per craft.
- The bar under the output shows the progress; hover the bar on the right to see the stored energy.

## Energy

| Property | Value |
|---|---|
| Energy type | Forge Energy (FE / RF) |
| Buffer | **200,000,000 FE** |
| Input limit | none (limited only by the cable) |
| Accepts energy from | every side |

## Automation

| Side | Items |
|---|---|
| **Top** | **Input, template style** (see below) |
| **Bottom** | **Output.** Pull the result from below. |
| Sides | no item access |

!!! tip "Template filling"
    Put one set of the recipe in the grid by hand. After that, items inserted from the top (hoppers, pipes,
    AE2 / Refined Storage) only **top up slots that already hold the same item**, always the one with the fewest
    items. Items that are not in the grid are refused, so the pattern is never broken.

## Recipe format (modpacks)

```json
{
  "type": "titanores:titan_crafting",
  "pattern": [
    "         ",
    "   AAA   ",
    "   ABA   ",
    "   AAA   ",
    "         ",
    "         "
  ],
  "key": {
    "A": {"item": "examplemod:item_a"},
    "B": {"tag": "forge:example_tag"}
  },
  "energy": 100000000,
  "time": 2400,
  "result": {"item": "examplemod:result_item", "count": 1}
}
```

The ids above are placeholders that only show the format.

| Field | Meaning |
|---|---|
| `pattern` | Exactly **6 rows of 9 characters**. Each character is one grid slot; a space means the slot must be empty. No offset or mirroring. |
| `key` | Symbol → ingredient. Items, tags (`{"tag": ...}`) and `forge:nbt` ingredients work. |
| `energy` | Total FE for one craft. |
| `time` | Ticks (20 ticks = 1 second). FE per tick = `energy / time`. |
| `result` | Output item and count. |
