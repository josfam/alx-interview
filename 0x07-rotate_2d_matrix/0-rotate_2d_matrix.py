#!/usr/bin/python3

"""Rotates a 2D n x n matrix in-place, by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix in-place, by 90 degrees clockwise.
    For this, it is assumed that the matrix will have 2 dimensions, and is not
    empty.
    """
    matrix_copy = [row[:] for row in matrix]

    n = len(matrix)
    row_to_replace = 0
    for col in range(n):
        column_nums = []
        for row in range(n - 1, -1, -1):  # bottom row going upwards
            value = matrix_copy[row][col]
            column_nums.append(value)
        # replace this row of numbers with those in from the column,
        # from left to right
        for idx, num in enumerate(column_nums):
            matrix[row_to_replace][idx] = num
        row_to_replace += 1
