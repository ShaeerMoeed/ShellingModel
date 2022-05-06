import numpy as np


def compute_happiness(p, index_x, index_y):

    dim = np.shape(p)[0]

    i = index_x
    j = index_y

    h = 0

    if p[i, j] == 1 or p[i, j] == 2:
        counter = 0
        if i == 0 and j == 0:
            if p[i+1, j] == p[i, j]:
                counter += 1
            if p[i, j+1] == p[i, j]:
                counter += 1
            if p[i+1, j+1] == p[i, j]:
                counter += 1
            h = counter/3
        elif i == dim-1 and j == dim-1:
            if p[i-1, j] == p[i, j]:
                counter += 1
            if p[i, j-1] == p[i, j]:
                counter += 1
            if p[i-1, j-1] == p[i, j]:
                counter += 1
            h = counter/3
        elif i == dim-1 and j == 0:
            if p[i-1, j] == p[i, j]:
                counter += 1
            if p[i, j+1] == p[i, j]:
                counter += 1
            if p[i-1, j+1] == p[i, j]:
                counter += 1
            h = counter/3
        elif i == 0 and j == dim-1:
            if p[i+1, j] == p[i, j]:
                counter += 1
            if p[i, j-1] == p[i, j]:
                counter += 1
            if p[i+1, j-1] == p[i, j]:
                counter += 1
            h = counter/3
        elif i == 0 and j != 0 and j != dim-1:
            if p[i, j-1] == p[i, j]:
                counter += 1
            if p[i, j+1] == p[i, j]:
                counter += 1
            if p[i+1, j-1] == p[i, j]:
                counter += 1
            if p[i+1, j] == p[i, j]:
                counter += 1
            if p[i+1, j+1] == p[i, j]:
                counter += 1
            h = counter/5
        elif i == dim-1 and j != 0 and j != dim-1:
            if p[i, j-1] == p[i, j]:
                counter += 1
            if p[i, j+1] == p[i, j]:
                counter += 1
            if p[i-1, j-1] == p[i, j]:
                counter += 1
            if p[i-1, j] == p[i, j]:
                counter += 1
            if p[i-1, j+1] == p[i, j]:
                counter += 1
            h = counter/5
        elif i != 0 and i != dim-1 and j == 0:
            if p[i-1, j] == p[i, j]:
                counter += 1
            if p[i+1, j] == p[i, j]:
                counter += 1
            if p[i-1, j+1] == p[i, j]:
                counter += 1
            if p[i, j+1] == p[i, j]:
                counter += 1
            if p[i+1, j+1] == p[i, j]:
                counter += 1
            h = counter/5
        elif i != 0 and i != dim-1 and j == dim-1:
            if p[i-1, j] == p[i, j]:
                counter += 1
            if p[i+1, j] == p[i, j]:
                counter += 1
            if p[i-1, j-1] == p[i, j]:
                counter += 1
            if p[i, j-1] == p[i, j]:
                counter += 1
            if p[i+1, j-1] == p[i, j]:
                counter += 1
            h = counter/5
        else:
            if p[i-1, j-1] == p[i, j]:
                counter += 1
            if p[i-1, j] == p[i, j]:
                counter += 1
            if p[i-1, j+1] == p[i, j]:
                counter += 1
            if p[i, j-1] == p[i, j]:
                counter += 1
            if p[i, j+1] == p[i, j]:
                counter += 1
            if p[i+1, j-1] == p[i, j]:
                counter += 1
            if p[i+1, j] == p[i, j]:
                counter += 1
            if p[i+1, j+1] == p[i, j]:
                counter += 1
            h = counter/8

    return h
