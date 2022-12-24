#!/usr/bin/python3
""" Return a list of integers repersenting the Pascal's triangl"""


def pascal_triangle(n):
    if n <= 0:
        return
    # height = 0
    T = [[1]]
    # loop for the next r = [1:height+1]
    for R in range(1, n):
        # c == 0
        N = [1]
        # caculate [1:r) (exclude r itself)
        for C in range(1, R):
            a = T[R - 1][C - 1]
            b = T[R - 1][C]
            # c = a + b
            N.append(a + b)
        # c == r
        N.append(1)
        T.append(N)
    return T
