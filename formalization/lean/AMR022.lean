import Mathlib.Tactic.NormNum

/-!
# Exact rational kernel for the AMR-022-5044 counterexample

This file formalizes the finite coefficient identity used by the manuscript's
headline witness. It does not formalize analytic power-series extraction or
the manuscript's every-index extension.
-/

namespace AMR022

/-- The degree-three coefficient obtained by finite binomial extraction from
`(1 + x*z)^alpha * (1-z)^(-beta)`. -/
def A3 (x alpha beta : ℚ) : ℚ :=
  beta * (beta + 1) * (beta + 2) / 6
    + alpha * beta * (beta + 1) / 2 * x
    + alpha * (alpha - 1) * beta / 2 * x ^ 2
    + alpha * (alpha - 1) * (alpha - 2) / 6 * x ^ 3

theorem witness_at_one : A3 1 (3 / 2) (1 / 14) = 33 / 686 := by
  norm_num [A3]

theorem witness_at_neg_one : A3 (-1) (3 / 2) (1 / 14) = 20 / 343 := by
  norm_num [A3]

/-- Kernel-checked exact certificate for the strict reverse inequality and
its gap at `(alpha,beta,j,x)=(3/2,1/14,3,-1)`. -/
theorem exact_counterexample :
    0 < A3 1 (3 / 2) (1 / 14) ∧
      |A3 (-1) (3 / 2) (1 / 14)| > A3 1 (3 / 2) (1 / 14) ∧
      |A3 (-1) (3 / 2) (1 / 14)| - A3 1 (3 / 2) (1 / 14) = 1 / 98 := by
  norm_num [A3, abs_of_nonneg]

end AMR022
