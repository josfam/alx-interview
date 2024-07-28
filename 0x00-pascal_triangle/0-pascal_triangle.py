#!/usr/bin/python3

"""Pascal's triangle interview question solution"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n rows"""
    if n <= 0:
        return []

    MAX_WINDOW_SIZE = 2
    ROWS_MADE = 1
    triangle = [[1]]
    pairs = []  # sliding window

    for _ in range(ROWS_MADE, n):
        last_row = triangle[-1]
        new_row = []  # new row to add to the triangle
        for num in last_row:
            if len(pairs) == MAX_WINDOW_SIZE:
                pairs.pop(0)
            pairs.append(num)
            new_row.append(sum(pairs))
        new_row.append(1)  # add the 1 in the last position
        triangle.append(new_row)
        pairs.clear()

    return triangle
