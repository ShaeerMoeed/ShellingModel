import numpy as np


def initial_threshold(p, red_threshold="random", blue_threshold="random"):

    dim = np.shape(p)[0]
    h = np.zeros([dim, dim])

    if red_threshold == "random" and blue_threshold == "random":
        for i in range(dim):
            for j in range(dim):
                if p[i, j] == 1 or p[i, j] == 2:
                    h[i, j] = (np.random.randint(50))/100

    if red_threshold == "random" and blue_threshold != "random":
        for i in range(dim):
            for j in range(dim):
                if p[i, j] == 1:
                    h[i, j] = (np.random.randint(50))/100
                elif p[i, j] == 2:
                    h[i, j] = float(blue_threshold)

    if red_threshold != "random" and blue_threshold == "random":
        for i in range(dim):
            for j in range(dim):
                if p[i, j] == 2:
                    h[i, j] = (np.random.randint(50))/100
                elif p[i, j] == 1:
                    h[i, j] = float(red_threshold)

    if red_threshold != "random" and blue_threshold != "random":
        for i in range(dim):
            for j in range(dim):
                if p[i, j] == 2:
                    h[i, j] = float(blue_threshold)
                elif p[i, j] == 1:
                    h[i, j] = float(red_threshold)

    return h



