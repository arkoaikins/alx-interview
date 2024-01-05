#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """Pascals Triangle"""
    if n <= 0:
        return []
    pascal = [[1]]
    for row_num in range(1, n):
        row = [1]
        for j in range(1, row_num):
            element = pascal[row_num - 1][j - 1] + pascal[row_num - 1][j]
            row.append(element)
        row.append(1)
        pascal.append(row)

    return pascal
