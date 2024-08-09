#!/usr/bin/python3

"""Finds the minimum number of operations needed to achieve a given number
of characters using only “Copy All” and “Paste” operations"""

from typing import List


def minOperations(n: int) -> int:
    """Calculates and returns the minimum number of operations to achieve a
    given number of characters using only “Copy All” and “Paste” operations
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    n_factors = []
    min_steps = 0
    i = 0

    # Find prime factors of n
    while n > 1:
        curr_prime = primes[i]
        if n % curr_prime == 0:
            n_factors.append(curr_prime)
            n = n // curr_prime
            continue
        i += 1
    return sum(n_factors)
