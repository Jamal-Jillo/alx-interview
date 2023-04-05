#!/usr/bin/env python3
"""Minimum Operations."""

import math


def minOperations(n):
    """Calculate the fewest number of operations needed to result in exactly n H characters in the file."""
    if n == 1:
        return 0

    # find prime factorization of n
    factors = {}
    i = 2
    while i*i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
                print(factors)
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
        print(factors)

    # calculate minimum number of operations
    min_ops = 0
    for exp in factors.values():
        min_ops += exp

    print(min_ops)
    return min_ops
