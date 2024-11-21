#!/usr/bin/python3
'''Rotate a 2D matrix by 90 degrees clockwise'''


def rotate_2d_matrix(mtx):
    '''Rotate matrix in-place by 90 degrees clockwise'''
    size = len(mtx)

    for r in range(size):
        for c in range(r, size):
            mtx[c][r], mtx[r][c] = mtx[r][c], mtx[c][r]

    for r in range(size):
        mtx[r] = mtx[r][::-1]
