#!/usr/bin/python3
import sys


def print_solution(board):
    """Print the current board configuration."""
    result = []
    for row in board:
        result.append([row[0], row[1]])
    print(result)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for r, c in board:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n, board, row):
    """Solve the N Queens problem using backtracking."""
    if row == n:
        print_solution(board)
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            found_solution = solve_nqueens(n, board, row + 1) or found_solution
            board.pop()

    return found_solution


def nqueens(n):
    """Solve the N Queens problem for a given N."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, [], 0)


def main():
    """Main entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)


if __name__ == "__main__":
    main()
