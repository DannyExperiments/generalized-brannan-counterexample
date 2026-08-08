# The problem and proof

For positive `alpha,beta`, define `A_n(x;alpha,beta)` by

```text
(1+xz)^alpha (1-z)^(-beta) = sum_(n>=0) A_n(x;alpha,beta) z^n.
```

Hayman--Lingham Problem 5.44 records the generalized question whether

```text
|A_j(x;alpha,beta)| <= A_j(1;alpha,beta)
```

for every `alpha,beta>0`, every odd `j>=3`, and every `|x|=1`.

The answer is **no**. Take

```text
alpha = 3/2, beta = 1/14, j = 3, x = -1.
```

Set `s=alpha+beta` and `d=alpha-beta`. Direct degree-three coefficient
extraction gives

```text
A_3(1)  = s(s^2-3d+2)/6,
A_3(-1) = -d(d-1)(d-2)/6.
```

At the stated parameters `s=11/7` and `d=10/7`, so

```text
A_3(1)     = 33/686 > 0,
|A_3(-1)|  = 20/343 = 40/686,
reverse gap = 1/98 > 0.
```

All hypotheses of the generalized assertion are met, and its conclusion is
strictly false. This is a complete negative answer to the literal all-positive
question. The witness has `alpha>1`, so it does not conflict with the known
unit-square theorem.

The paper proves two additional results: an exact iff classification of the
degree-three endpoint inequality and rational positive-right-hand-side
counterexamples at every integer index `j>=3`.
