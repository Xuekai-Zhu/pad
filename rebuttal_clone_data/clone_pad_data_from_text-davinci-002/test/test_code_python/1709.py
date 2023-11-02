def solution():
    pool_length = 10
    pool_width = 8
    pool_depth = 6
    pool_volume = pool_length * pool_width * pool_depth
    quarts_per_pool = pool_volume / 120
    cost_per_quart = 3
    total_cost = quarts_per_pool * cost_per_quart
    result = total_cost
    return result

print(solution())