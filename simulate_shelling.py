import numpy as np
import compute_happiness as ch
import initial_threshold as it
import move as m
import populate_world as pw
import matplotlib.pyplot as plt


def simulate_shelling(n_red, n_blue, n_grid, cycles, max_attempts, red_threshold_input, blue_threshold_input):

    p = pw.populate_world(n_red, n_blue, n_grid)

    t = it.initial_threshold(p, red_threshold=red_threshold_input, blue_threshold=blue_threshold_input)

    time_step = 0
    while time_step < cycles:

        time_step += 1

        x_blue = np.zeros(n_blue)
        y_blue = np.zeros(n_blue)
        x_red = np.zeros(n_red)
        y_red = np.zeros(n_red)
        counter_red = 0
        counter_blue = 0

        for i in range(n_grid):
            for j in range(n_grid):

                if p[i, j] == 1:
                    x_red[counter_red] = float(i)
                    y_red[counter_red] = float(j)
                    counter_red += 1

                elif p[i, j] == 2:
                    x_blue[counter_blue] = float(i)
                    y_blue[counter_blue] = float(j)
                    counter_blue += 1

        for i in range(n_grid):
            for j in range(n_grid):

                if p[i, j] == 1:
                    h = ch.compute_happiness(p, i, j)
                    if h < t[i, j]:
                        updated_state = m.move(p, t, i, j, max_attempts)
                        p = updated_state[0]
                        t = updated_state[1]

                elif p[i, j] == 2:
                    h = ch.compute_happiness(p, i, j)
                    if h < t[i, j]:
                        updated_state = m.move(p, t, i, j, max_attempts)
                        p = updated_state[0]
                        t = updated_state[1]

        f = plt.figure()
        plt.plot(x_blue, y_blue, 'ob')
        plt.plot(x_red, y_red, 'or')
        plt.show()
        f.clear()

    return p, t
