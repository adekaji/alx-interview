#!/usr/bin/python3
""" Given an n x n 2D matrix, rotate it 90 degrees clockwise
"""

def print_rotated_matrix(matrix):
    """print rotated 2D amtrix
    """
    row, col = len(matrix), len(matrix[0])

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end="  ")
        print()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    right_rotate(matrix)
    print_rotated_matrix(matrix)
    print("--------")

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    left_rotate(matrix)
    print_rotated_matrix(matrix)
