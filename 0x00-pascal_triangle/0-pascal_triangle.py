#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    '''Draws Pascal's Triangle'''
    arr = []
    if n <= 0:
        return arr

    result = [1]
    arr.append(result)
    for i in range(1, n):
        temp = [0] + result + [0]
        result = []
        for j in range(len(temp) - 1):
            result.append(temp[j] + temp[j + 1])
        arr.append(result)

    return arr
