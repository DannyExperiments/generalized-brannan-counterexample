# Reproducibility

The exact arithmetic replay uses only the Python standard library.

```text
python3 checks/verify_counterexample.py
```

Its six output lines must match `checks/EXPECTED_OUTPUT.txt` exactly. The
script is corroboration, not a substitute for the symbolic proof in the
manuscript.

The complete repository check is:

```text
python3 scripts/verify_repository.py
```

It verifies the checksum ledger, required public files, scope markers, privacy
patterns, and the exact verifier output. The GitHub workflow `verify.yml` runs
the same command on every push and pull request.

The manuscript build is documented in `paper/BUILD.md` and replayed by
`.github/workflows/pdf.yml`. The PDF workflow starts from TeX and the
bibliography; a committed PDF is not accepted as build evidence by itself.
Volatile pdfTeX metadata is suppressed, so a clean build with the pinned CI
toolchain is expected to be byte-identical to the committed PDF.

`release/EVIDENCE_BUNDLE.zip` is a deterministic, public-safe subset containing
the shortest proof, exact arithmetic replay, public audit summaries, and the
pinned partial Lean project. It deliberately excludes private model receipts
and third-party source PDFs.

Rebuild it with:

```text
python3 scripts/build_evidence_bundle.py
```

Two builds from unchanged inputs produce byte-identical ZIP archives.
