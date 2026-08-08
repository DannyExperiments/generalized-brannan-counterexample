# Partial Lean verification

`AMR022.lean` kernel-checks the exact rational degree-three coefficient formula
at the headline witness and proves the strict reverse inequality with gap
`1/98`.

This is deliberately narrower than the manuscript. It does not formalize the
analytic derivation of the finite coefficient formula, the complete endpoint
classification, or the every-index construction.

Pinned toolchain: Lean and Mathlib `v4.30.0`.

```bash
lake build
lake env lean AMR022.lean
lake env lean -Dpp.universes=true -Dpp.all=false Axioms.lean
```
