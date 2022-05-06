import numpy as np
from compute_happiness import compute_happiness as ch


def move(p, t, index_x, index_y, max_attempts):

    dim = np.shape(p)[0]
    p_updated = np.copy(p)
    t_updated = np.copy(t)

    attempts = max_attempts
    while attempts > 0:

        attempts -= 1

        updated_i = np.random.randint(dim)
        updated_j = np.random.randint(dim)

        if p[updated_i, updated_j] == 0:
            if ch(p, updated_i, updated_j) < t[index_x, index_y]:
                p_updated[updated_i, updated_j] = p[index_x, index_y]
                p_updated[index_x, index_y] = 0
                t_updated[updated_i, updated_j] = t[index_x, index_y]
                t_updated[index_x, index_y] = 0
                break

    return p_updated, t_updated


