#!/usr/bin/env python3
"""Minimum Operations."""


def minOperations(n):
    """Calculate the fewest number of operations needed."""
    if n < 1:
        return 0

    i = 2
    operations = 0

    while n > 1:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    return operations
