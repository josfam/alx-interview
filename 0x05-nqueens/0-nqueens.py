#!/usr/bin/python3

"""Arranging N Queens on a chess board with backtracking"""

import sys


def get_n_queens():
    """Gets the possible solutions for placing n queens on a chess board, such
    that now two queens attack each other
    """
    if not len(sys.argv) == 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        queens = int(sys.argv[1])
    except ValueError as e:
        print('N must be a number')
        sys.exit(1)
    if queens < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = []
    place_queens(row=0, n=queens, curr_soln=[], solutions=solutions)
    return solutions


def place_queens(row, n, curr_soln, solutions):
    """Places n queens in an n x n chess board, such that no queens attack
    each other

    Args
        row: The current row of the board where a queen is being placed
        n: The number of queens to place
        curr_soln: The current solution state being explored
        solutions: The valid solutions found so far
    """
    # base case:
    if row == n:  # all rows exhausted
        solutions.append(curr_soln.copy())
        return

    # recursive case
    for col in range(n):
        if is_legal_spot(row, col, curr_soln):
            # place the queen
            curr_soln.append([row, col])

            # place the next queen in the next row
            place_queens(row + 1, n, curr_soln, solutions)

            # met a dead end
            curr_soln.pop()


def is_legal_spot(row, col, curr_soln):
    """Returns True if this location on the board is a legal, non-conflicting
    spot to put this queen. A spot is legal if no other queens already appear
    in the same row, column, or diagonals as the queen currently being placed.

    Args:
        row: The current row that a queen is being placed
        col: The current column that a queen is being placed
        curr_soln: The current solution state being explored
    """

    for queen_loc in curr_soln:
        queen_row, queen_col = queen_loc
        # queens cannot be on the same column
        if (queen_col == col) or (queen_row == row):
            return False
        # two queens cannot be on the same major diagonal
        if (row - col) == (queen_row - queen_col):
            return False
        # two queens cannot be on the same minor diagonal
        if (row + col) == (queen_row + queen_col):
            return False
    return True


solutions = get_n_queens()

for solution in solutions:
    print(solution)
