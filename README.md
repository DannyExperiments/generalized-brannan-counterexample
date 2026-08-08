# Counterexamples to an all-positive Brannan coefficient inequality

[![Verify public evidence](https://github.com/DannyExperiments/generalized-brannan-counterexample/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/generalized-brannan-counterexample/actions/workflows/verify.yml)
[![PDF build](https://github.com/DannyExperiments/generalized-brannan-counterexample/actions/workflows/pdf.yml/badge.svg)](https://github.com/DannyExperiments/generalized-brannan-counterexample/actions/workflows/pdf.yml)
[![Partial exact-witness Lean check](https://github.com/DannyExperiments/generalized-brannan-counterexample/actions/workflows/lean.yml/badge.svg)](https://github.com/DannyExperiments/generalized-brannan-counterexample/actions/workflows/lean.yml)

[Paper (PDF)](paper/manuscript.pdf) ·
[TeX source](paper/manuscript.tex) ·
[Problem and proof](proof/PROBLEM_AND_PROOF.md) ·
[Mathematical audit](audits/MATHEMATICAL_AUDIT.md) ·
[Literature audit](audits/LITERATURE_PRIORITY_AUDIT.md) ·
[Reproduce](REPRODUCIBILITY.md)

This repository gives a negative answer to the literal all-positive
generalized coefficient question recorded as Hayman--Lingham Problem 5.44.
For

```text
(1+xz)^alpha(1-z)^(-beta) = sum_(n>=0) A_n(x;alpha,beta) z^n,
```

the problem asks whether

```text
|A_j(x;alpha,beta)| <= A_j(1;alpha,beta)
```

holds for every `alpha,beta>0`, every odd `j>=3`, and every `|x|=1`.
The answer is **no**. The exact admissible witness

```text
(alpha,beta,j,x) = (3/2,1/14,3,-1)
```

satisfies

```text
A_3(1)      = 33/686 > 0,
|A_3(-1)|   = 20/343 = 40/686,
reverse gap = 1/98 > 0.
```

This is a complete negative answer to the unrestricted positive-parameter
question. It does **not** disprove the classical theorem on
`0<alpha,beta<=1`.

## Stronger results

The manuscript also proves:

- the exact iff classification
  `|A_3(-1)| <= A_3(1)` precisely when
  `3 beta(beta+1)+(alpha-1)(alpha-2) >= 0`;
- the exact equality wall and reverse-gap formula; and
- rational positive-right-hand-side counterexamples at every integer index
  `j>=3`, hence at every odd index covered by the recorded problem.

## Verification and scope

| Gate | Status |
|---|---|
| Exact symbolic counterexample | Complete |
| Mathematical audit | Three independent audits, authorized repair, and three delta passes |
| Exact arithmetic replay | Pass; non-load-bearing |
| Literature search | Three documented lanes through August 6, 2026 |
| Priority language | Apparently new, moderate confidence; absolute priority not claimed |
| Human specialist review | Not obtained |
| Formalization | Lean 4.30.0 kernel-checks the exact rational witness, strict reverse inequality, and gap `1/98`; analytic and every-index results are not formalized |
| Manuscript | Four-page PDF cleanly rebuilt; checksum and page-by-page visual preflight passed |

The remaining historical uncertainty is concrete: complete older theses and
dissertations of Udaya C. Jayatilake, related seminar materials, restricted
older chapters and reports, and private or non-digitized sources were not all
retrievable. No publicly retrievable identical or stronger counterexample was
found in the documented search.

## Repository map

- [`paper/`](paper/) — manuscript source, bibliography, PDF, and build record.
- [`proof/`](proof/) — the exact question and shortest counterexample proof.
- [`audits/`](audits/) — public-safe mathematical and literature adjudications.
- [`checks/`](checks/) — dependency-free exact rational replay.
- [`scripts/`](scripts/) — repository integrity, scope, privacy, and replay checks.
- [`formalization/`](formalization/) — pinned partial exact-witness Lean certificate and exact scope.
- [`evidence/`](evidence/) — sanitized process summary; raw private receipts are excluded.

## Authorship and AI disclosure

The final authorship and public AI-disclosure wording remain explicit human
release decisions. AI systems were used for discovery, proof development,
adversarial auditing, literature-search assistance, manuscript preparation,
and repository assembly. No AI system is proposed as an author. See
[`AI_ASSISTANCE.md`](AI_ASSISTANCE.md) and [`PROVENANCE.md`](PROVENANCE.md).

This repository is a private release candidate until the remaining gates in
[`STATUS.md`](STATUS.md) are approved. The local evidence and PDF workflows are
defined above; their badges become release evidence only after all three workflows
pass on the eventual repository's default branch. It does not claim journal
acceptance, human peer review, full analytic formalization, or absolute
historical priority.
