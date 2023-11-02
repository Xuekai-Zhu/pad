def solution():
    doubling_time = 20 # in minutes
    growth_period = 240 # in minutes (4 hours)
    initial_cells = 1

    # Calculate the number of doubling periods that occur during the growth period
    num_doubling_periods = growth_period / doubling_time

    # Calculate the total number of cells after the growth period
    total_cells = initial_cells * (2 ** num_doubling_periods)
    result = total_cells
    return result

print(solution())