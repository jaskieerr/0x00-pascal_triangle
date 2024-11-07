import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen on board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N Queens problem using backtracking.
    """
    def backtrack(board, col):
        """
        Recursive function to solve the N Queens problem.
        """
        # Base case: If all queens are placed, return True
        if col == n:
            solutions.append([row[:] for row in board])
            return True

        # Place this queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1

                # Recur to place rest of the queens
                backtrack(board, col + 1)

                # If placing a queen in board[i][col] doesn't lead to a solution, remove the queen
                board[i][col] = 0

    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print([(i, solution.index(1)) for i, val in enumerate(solution) if val == 1])
