#!/usr/bin/python3
"""
 Rotates matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates matrix 90 degrees clockwise
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
