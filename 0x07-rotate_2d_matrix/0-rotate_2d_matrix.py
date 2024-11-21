#!/usr/bin/python3
"""Rotate a 2D matrix by 90 degrees clockwise."""

def rotate_2d_matrix(matrix):
    """Rotate matrix in-place by 90 degrees clockwise."""
    size = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for row in range(size):
        for col in range(row, size):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    # Reverse each row to complete the rotation
    for row in range(size):
        matrix[row] = matrix[row][::-1]
