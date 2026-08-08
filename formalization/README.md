# Formalization status

The pinned Lean 4.30.0/Mathlib 4.30.0 project in [`lean/`](lean/) checks the
finite rational kernel of the headline counterexample:

- the displayed degree-three coefficient formula at `x=1` equals `33/686`;
- the same formula at `x=-1` equals `20/343`;
- its absolute value strictly exceeds the value at `x=1`; and
- the reverse gap is exactly `1/98`.

The clean local build passed, and `#print axioms` reports only `propext`,
`Classical.choice`, and `Quot.sound` for the three public declarations.

This is a **partial exact-witness formalization**. It does not formalize the
analytic power-series derivation of the coefficient formula, the endpoint
classification, or the every-index construction. The badge and workflow use
that limited description deliberately.
