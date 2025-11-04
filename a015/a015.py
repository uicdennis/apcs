import numpy as np
import os

def dimension(matrix: list) -> tuple[int, int]:
    m = len(matrix)
    if isinstance(matrix[0], list):
        n = len(matrix[0])
    else:
        n = 1
    return m, n

def transport_without_numpy(matrix: list) -> list:
    m, n = dimension(matrix)
    T = []
    for i in range(n):
        lst = []
        for j in range(m):
            lst.append(matrix[j][i])
        T.append(lst)
    return T

def transport_with_numpy(matrix: list) -> list:
    A = np.array(matrix)
    # print(A.dumps())
    return A.T

def show_array_elements(matrix: list):
    m, n = dimension(matrix)
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

def test():
    A = [[3, 1, 2], [8, 5, 4]]
    print(dimension(A))
    print(show_array_elements(transport_without_numpy(A)))

    print(show_array_elements(transport_with_numpy(A).tolist()))

    # A = np.array([[3, 1, 2], [8, 5, 4]])
    # print(type(A))
    # print(A.T)
    # print(A.shape)
    # print(A.size)

if __name__ == "__main__":

    filename = input()
    path = os.getcwd()
    if path.split('\\')[-1] != 'a015':
        filename = path + '\\a015\\' + filename
    else:
        filename = path + '\\' + filename
    # dir = os.curdir
    fd = open(filename, 'rt', encoding="utf-8")
    lines = fd.readlines()
    begin_idx = 0
    idx = 0
    total = len(lines)
    while idx < total:
        dims = lines[idx].split()
        m = int(dims[0])
        n = int(dims[1])
        A = []
        idx += 1
        for line in lines[idx:(idx+m)]:
            A.append([int(x) for x in line.split()])
        show_array_elements(transport_without_numpy(A))
        idx += m
