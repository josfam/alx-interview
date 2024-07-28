#!/usr/bin/env python3
"""Pascal's triangle interview question solution"""

from collections import deque

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n == 0:
        return []

    triangle = [[1]]
    ROWS_MADE = 1
    pairs = deque(maxlen=2) # sliding window

    for _ in range(ROWS_MADE, n):
        last_row = triangle[-1]
        new_row = []  # new row to add to the triangle
        for num in last_row:
            pairs.append(num)
            new_row.append(sum(pairs))
        new_row.append(1) # add the 1 in the last position
        triangle.append(new_row)
        pairs.clear()

    return triangle
