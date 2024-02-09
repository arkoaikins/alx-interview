#!/usr/bin/python3
import sys


def is_valid(queens, row, col):
    """Check if queen attacks any existing queens"""
    for r in range(row):
        if queens[r] == col or abs(queens[r] - col) == abs(r - row):
            return False
    return True


def solve_n_queens(queens, row, n):
    # Base case: all queens placed
    if row == n:
        # Print solution in requested format
        solution = [[r, col] for r, col in enumerate(queens)]
        print(solution)
        return

    # Try placing queen in each column
    for col in range(n):
        if is_valid(queens, row, col):
            queens[row] = col
            solve_n_queens(queens, row + 1, n)


def main():
    """solves the n quees puzzle"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    # Initialize empty board
    queens = [-1] * n
    # Solve and print solutions
    solve_n_queens(queens, 0, n)


if __name__ == "__main__":
    main()
