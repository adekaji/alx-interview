#!/usr/bin/python3
"""
Define a function that rotates an nxn 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90 degrees clockwise in-place
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    N = len(matrix)

    # transpose matrix
    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse matrix
    for i in range(N):
        for j in range(N//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N-j-1]
            matrix[i][N-j-1] = temp
