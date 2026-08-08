# Repository manifest

## Public-facing mathematical scope

- `README.md`
- `ORIGINAL_PROBLEM.md`
- `CLAIM_SCOPE_AND_LIMITATIONS.md`
- `PRIOR_ART_AND_LIMITATIONS.md`
- `STATUS.md`
- `CITATION.cff`
- `CLAIMS_EVIDENCE_MATRIX.md`
- `CONTRIBUTING.md`
- `LICENSE_STATUS.md`
- `SECURITY.md`

## Reproducibility

- `REPRODUCIBILITY.md`
- `scripts/verify_repository.py`
- `checks/verify_counterexample.py`
- `checks/EXPECTED_OUTPUT.txt`
- `.github/workflows/verify.yml`
- `.github/workflows/pdf.yml`
- `.github/workflows/lean.yml`

## Paper and readable proof

- `paper/manuscript.tex`
- `paper/manuscript.pdf`
- `paper/references.bib`
- `paper/README.md`
- `paper/BUILD.md`
- `paper/BUILD_LOG.txt`
- `paper/PDF_PREFLIGHT.txt`
- `paper/MANUSCRIPT_COMPARISON.md`
- `proof/PROBLEM_AND_PROOF.md`

## Evidence and process disclosure

- `evidence/AUDIT_SUMMARY.md`
- `evidence/README.md`
- `audits/MATHEMATICAL_AUDIT.md`
- `audits/LITERATURE_PRIORITY_AUDIT.md`
- `AI_DISCLOSURE.md`
- `PROVENANCE.md`

## Formalization status

- `formalization/README.md`
- `formalization/lean/AMR022.lean`
- `formalization/lean/Axioms.lean`
- `formalization/lean/LEAN_AXIOMS.txt`
- `formalization/lean/README.md`
- `formalization/lean/lakefile.toml`
- `formalization/lean/lake-manifest.json`
- `formalization/lean/lean-toolchain`

## Release staging

- `release/README.md`
- `release/RELEASE_NOTES_DRAFT.md`
- `release/zenodo_metadata_draft.json`
- `release/EVIDENCE_BUNDLE.zip`

## Repository tooling

- `scripts/verify_repository.py`
- `scripts/build_evidence_bundle.py`
- `scripts/verify.sh`

`SHA256SUMS.txt` covers every other regular file in this release. The clean
PDF build, page-by-page visual preflight, local checksum replay, exact arithmetic
replay, repository verifier, and all three public-branch workflows have passed.
Authorship, license status, citation metadata, and publication visibility are
approved. The immutable Version 1.0.0 deposit is published and verified at
`https://doi.org/10.5281/zenodo.21853316`.
