#!/usr/bin/python3
""" 0x07. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise in-place.
    """
    # Replica Matrix
    replica = matrix[:]

    for i in range(len(matrix)):
        # retract column from replica
        column = [row[i] for row in replica]
        # Replace in matrix in reverse order
        matrix[i] = column[::-1]
