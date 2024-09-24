#!/usr/bin/python3

"""Determines the fewest number of coins needed to meet a given amount total
using a greedy algorithm"""

import time


def makeChange(coins, total):
    """
    Args:
        coins: A list of values of coins in our possession. It is assumed that
        there is an infinite number of each coin
        total: The total amount of change to get by combining the coins in our
        possession.
    Returns:
        The fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    min_coins = 0
    sorted_coins = list(reversed(sorted(coins)))
    for coin in sorted_coins:
        while total >= coin:
            min_coins += total // coin
            total = total % coin

    if total != 0:  # not all coins could be divided
        return -1
    return min_coins
