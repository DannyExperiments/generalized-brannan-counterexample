# Problem 5.44: generalized coefficient inequality

For positive real parameters `alpha,beta` and `|x|=1`, define the coefficients
by the analytic expansion at the origin

```text
(1+xz)^alpha (1-z)^(-beta) = sum_(n>=0) A_n(x;alpha,beta) z^n.
```

The generalized question recorded in Hayman--Lingham, *Research Problems in
Function Theory*, Problem 5.44, asks whether

```text
|A_j(x;alpha,beta)| <= A_j(1;alpha,beta)
```

for all `alpha,beta>0`, all odd integers `j>=3`, and all `|x|=1`.

The repository's answer is **no**. The exact witness

```text
(alpha,beta,j,x)=(3/2,1/14,3,-1)
```

has `A_3(1)=33/686>0`, `|A_3(-1)|=20/343`, and reverse gap
`1/98`.

The condition that at least one parameter exceed `1` is a search reduction
obtained after applying the known theorem on `(0,1]^2`; it is not part of the
literal source quantifiers.
