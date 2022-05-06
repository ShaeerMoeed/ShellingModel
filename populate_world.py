import numpy as np


def populate_world(n_red, n_blue, n_grid):

    p = np.zeros([n_grid, n_grid])

    available_red = n_red
    available_blue = n_blue
    available_empty = n_grid**2 - n_blue - n_red
    for i in range(n_grid):
        for j in range(n_grid):
            if available_red > 0 and available_blue > 0 and available_empty > 0:
                p[i, j] = np.random.randint(3)
                if p[i, j] == 0:
                    available_empty -= 1
                if p[i, j] == 1: 
                    available_red -= 1
                elif p[i, j] == 2:
                    available_blue -= 1
            elif available_red > 0 and available_blue > 0 and available_empty == 0:
                p[i, j] = np.random.randint(1, 2)
                if p[i, j] == 1:
                    available_red -= 1
                elif p[i, j] == 2:
                    available_blue -= 1
            elif available_red > 0 and available_blue == 0 and available_empty > 0:
                p[i, j] = np.random.randint(2)
                if p[i, j] == 0:
                    available_empty -= 1
                if p[i, j] == 1:
                    available_red -= 1
            elif available_red > 0 and available_blue == 0 and available_empty == 0:
                p[i, j] = 1
                available_red -= 1
            elif available_red == 0 and available_blue > 0 and available_empty > 0:
                p[i, j] = np.random.randint(2)
                if p[i, j] == 0:
                    available_empty -= 1
                if p[i, j] == 1:
                    p[i, j] = 2
                    available_blue -= 1
            elif available_red == 0 and available_blue > 0 and available_empty == 0:
                p[i, j] = 2
                available_blue -= 1
            elif available_red == 0 and available_blue == 0 and available_empty > 0:
                p[i, j] = 0
                available_empty -= 1
            elif available_red == 0 and available_blue == 0 and available_empty == 0:
                raise ValueError("Array indices not exhausted but there are no available valid entries.")

    return p
