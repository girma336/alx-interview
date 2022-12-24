#!/usr/bin/python3
""" Return a list of integers repersenting the Pascal's triangl"""


def pascal_triangle(n):
    if n <= 0:
        return
    Triangle = [[1]]
    for R in range(1, n):
        NewValue = [1]
        for C in range(1, R):
            numOne = Triangle[R - 1][C - 1]
            numTwo = Triangle[R - 1][C]
            NewValue.append(numOne + numTwo)
        NewValue.append(1)
        Triangle.append(NewValue)
    return Triangle
