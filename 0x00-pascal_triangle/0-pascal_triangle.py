#!/usr/bin/python3
"""Module that contains the pascal_triangle function."""


def pascal_triangle(n):
    """Functions that returns a list of lists of integers.

representing the Pascal’s triangle of n.
"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1] + [prev_row[j] + prev_row[j+1] for j in range(len(prev_row)-1)] + [1]
        triangle.append(curr_row)
    return triangle
