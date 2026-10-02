# TitanOres Docs

Documentation site for **TitanOres**, the endgame ore progression mod of the Titan Modpack
(Minecraft 1.16.5 / Forge 36.2.42). Built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
and published with GitHub Pages.

The mod itself lives in a separate repository: [pedroedu06/TitanOres](https://github.com/pedroedu06/TitanOres).

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000. Pages reload on save.

## Sync with the mod

Icons and recipe grids are generated from the mod's own files. After changing the mod, run:

```bash
python scripts/sync_from_mod.py ../TitanOres
```

It copies item icons to `docs/assets/icons/` and writes one HTML snippet per recipe to `docs/snippets/recipes/`.
Pages include a recipe with:

```html
<div class="recipes">
--8<-- "recipes/solarite_block.html"
</div>
```

All pages live at the root of `docs/` (the recipe snippets use relative icon paths); the menu hierarchy is set in
`mkdocs.yml` under `nav`.

## Publish

Every push to `main` runs `.github/workflows/deploy.yml`, which builds the site and pushes it to the `gh-pages`
branch. In the GitHub repository settings, set **Pages → Source** to the `gh-pages` branch.

## License

TitanOres © Pedro. All Rights Reserved.
