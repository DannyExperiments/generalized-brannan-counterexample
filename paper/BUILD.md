# Build instructions

Required local tools:

- a TeX distribution containing `amsart`, `geometry`, `microtype`,
  `mathtools`, `amssymb`, and `hyperref`;
- `latexmk` and BibTeX.

From this directory run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

For a clean replay:

```bash
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

The repository's PDF workflow performs the same clean build without fetching
project dependencies.
