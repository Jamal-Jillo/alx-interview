#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """Prime Game."""
    maria_wins = 0
    ben_wins = 0

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(x):
        primes = []
        for num in range(1, nums[i] + 1):
            if is_prime(num):
                primes.append(num)

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
