# Build instructions

Required local tools:

- a TeX distribution containing `amsart`, `geometry`, `microtype`,
  `mathtools`, `amssymb`, and `hyperref`;
- `latexmk` and BibTeX.

From this directory run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
```

For a clean replay:

```bash
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
```

The repository's PDF workflow deletes the committed PDF, performs the same
clean source build without fetching project dependencies, and fails if the
final log contains unresolved references or citations, multiply defined
labels, overfull or underfull boxes, or LaTeX errors.

The source suppresses volatile pdfTeX creation/modification timestamps,
trailer IDs, and PTEX banner data. With the pinned CI toolchain and unchanged
inputs, repeated clean builds must therefore produce a byte-identical PDF.
