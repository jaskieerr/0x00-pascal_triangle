#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    p_triangle = [[1]]
    for r in range(1, n):
        new_row = [1]
        for i in range(1, r):
            element = p_triangle[r - 1][i - 1] + p_triangle[r - 1][i]
            new_row.append(element)
        new_row.append(1)
        p_triangle.append(new_row)

    return p_triangle
