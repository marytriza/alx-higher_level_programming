#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_values = [[x * x for x in y] for y in matrix]
    return square_values
