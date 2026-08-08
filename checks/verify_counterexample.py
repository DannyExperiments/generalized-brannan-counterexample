#!/usr/bin/env python3
"""Dependency-free exact replay of the three independently found witnesses."""

from fractions import Fraction as Q
from math import factorial


def falling_binomial(a: Q, k: int) -> Q:
    value = Q(1)
    for i in range(k):
        value *= a - i
    return value / factorial(k)


def rising(a: Q, k: int) -> Q:
    value = Q(1)
    for i in range(k):
        value *= a + i
    return value


def coefficients(a: Q, b: Q, j: int = 3) -> list[Q]:
    return [
        falling_binomial(a, k) * rising(b, j - k) / factorial(j - k)
        for k in range(j + 1)
    ]


def at_sign(coeffs: list[Q], sign: int) -> Q:
    return sum(((Q(sign) ** k) * c for k, c in enumerate(coeffs)), Q(0))


def check_minus_one(a: Q, b: Q, expected_a1: Q,
                    expected_am1: Q, expected_gap: Q) -> None:
    coeffs = coefficients(a, b)
    a1 = at_sign(coeffs, 1)
    am1 = at_sign(coeffs, -1)
    assert a1 == expected_a1 > 0
    assert am1 == expected_am1
    assert abs(am1) - a1 == expected_gap > 0


def main() -> None:
    c = coefficients(Q(3, 2), Q(1, 6))
    assert c == [Q(91, 1296), Q(7, 48), Q(1, 16), Q(-1, 16)]
    a1 = at_sign(c, 1)
    u = c[0] - c[2] - c[3]
    v = c[1] + c[2]
    assert a1 == Q(35, 162) > 0
    assert u * u + u * v + v * v - a1 * a1 == Q(1013, 62208) > 0

    check_minus_one(Q(3, 2), Q(1, 14), Q(33, 686), Q(20, 343), Q(1, 98))
    check_minus_one(Q(5, 4), Q(1, 20), Q(39, 2000), Q(4, 125), Q(1, 80))

    print("BLIND_ZETA_WITNESS=PASS")
    print("M13_MINUS_ONE_WITNESS=PASS")
    print("M01_MINUS_ONE_WITNESS=PASS")
    print("RIGHT_HAND_SIDES_POSITIVE=PASS")
    print("MINIMUM_ALLOWED_INDEX_J3=PASS")
    print("UNIVERSAL_ASSERTION_REFUTED=YES")


if __name__ == "__main__":
    main()
