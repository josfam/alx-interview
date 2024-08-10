#!/usr/bin/python3

"""Finds the minimum number of operations needed to achieve a given number
of characters using only “Copy All” and “Paste” operations"""

from typing import List


def isPrime(n) -> bool:
    """Checks if a number is a prime number"""
    if n < 2:
        return False
    root_n = int(n ** 0.5)
    for i in range(2, root_n + 1):  # stop on square root for efficiency
        if n % i == 0:
            return False
    return True


def minOperations(n: int) -> int:
    """Calculates and returns the minimum number of operations to achieve a
    given number of characters using only “Copy All” and “Paste” operations
    """
    if (n < 1):
        return 0

    minOperations = 0
    curr_num = 2
    root_n = int(n ** 0.5)

    # Find prime factors of n
    while curr_num <= n:
        if n % curr_num == 0:
            minOperations += curr_num
            n = n // curr_num
        else:
            # find the next prime number
            curr_num += 1
            while (not isPrime(curr_num)) and (curr_num <= n):
                curr_num += 1
    return minOperations
