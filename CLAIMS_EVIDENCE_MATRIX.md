# Claims–evidence matrix

| Public claim | Mathematical source | Independent support | Boundary |
|---|---|---|---|
| The all-positive question in Hayman–Lingham Problem 5.44 has a negative answer | `paper/manuscript.tex`, Theorem 1 | Three mathematical audit lanes, one authorized repair, and three delta passes | No human specialist review |
| `(alpha,beta,j,x)=(3/2,1/14,3,-1)` is an exact witness with reverse gap `1/98` | `proof/PROBLEM_AND_PROOF.md` | Symbolic proof, dependency-free rational replay, and partial Lean certificate | Computation is corroborating, not load-bearing |
| The degree-three endpoint inequality has the stated iff classification | `paper/manuscript.tex`, Theorem 2 | Reconstructed in the mathematical audits | Not formalized in Lean |
| Counterexamples exist at every integer index `j>=3` | `paper/manuscript.tex`, Theorem 3 | Reconstructed in the mathematical audits | Not formalized in Lean |
| The classical unit-square theorem is not contradicted | `CLAIM_SCOPE_AND_LIMITATIONS.md` and manuscript introduction | Scope audits and primary-source comparison | The result concerns unrestricted positive parameters |
| No publicly retrievable identical or stronger counterexample was located through 2026-08-06 | `audits/LITERATURE_PRIORITY_AUDIT.md` | Three documented priority-search lanes | Apparently new, moderate confidence; absolute priority not claimed |
| Lean checks the exact rational witness and strict gap | `formalization/lean/AMR022.lean` | Pinned Lean/Mathlib build and axiom report | Analytic extraction and the every-index theorem are outside scope |
| Repository artifacts are byte-identified and replayable | `MANIFEST.md`, `SHA256SUMS.txt`, `scripts/verify_repository.py` | Local replay and GitHub Actions | Hashes and CI do not prove the mathematics |
