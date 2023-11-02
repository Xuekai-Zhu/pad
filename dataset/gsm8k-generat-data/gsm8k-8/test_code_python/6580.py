def solution():
    # Calculate the total amount of water needed to fill the pool
    pool_size = 50000  # in gallons
    water_needed = pool_size * 1.0

    # Calculate the total cost of the water
    water_cost = water_needed / 10.0 * 0.01

    # Calculate the total time it takes to fill the pool
    time_needed = pool_size / 100.0  # in hours

    result = water_cost
    return result

print(solution())