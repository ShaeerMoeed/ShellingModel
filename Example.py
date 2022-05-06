import simulate_shelling as ss

n_red = 1000
n_blue = 1000
n_grid = 50
cycles = 20
max_attempts = 100
red_threshold_input = "0.2"
blue_threshold_input = "0.2"

ss.simulate_shelling(n_red, n_blue, n_grid, cycles, max_attempts, red_threshold_input, blue_threshold_input)