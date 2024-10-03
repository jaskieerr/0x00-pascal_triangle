#!/usr/bin/python3
'''pascale triangle exercise'''


def pascal_triangle(n):
    '''func'''
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        i = [1]
        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            i.append(element)
        i.append(1)
        triangle.append(i)

    return triangle
