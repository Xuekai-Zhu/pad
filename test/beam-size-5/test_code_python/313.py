def solution():
    pool_length = 6
    pool_width = 4
    pool_depth = pool_length * pool_width
    cost_per_cubic_foot = 0.1

    # Calculate the volume of the pool
    pool_volume = pool_length * pool_width

    # Calculate the total cost to fill the pool
    total_cost = pool_volume * cost_per_cubic_foot
    result = total_cost
    return result

print(solution())