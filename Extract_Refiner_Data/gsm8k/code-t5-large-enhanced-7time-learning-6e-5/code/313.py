def solution():
    
    pool_depth = 5
    pool_width = 6
    pool_length = 4
    pool_volume = pool_depth * pool_width * pool_length
    cost_per_cubic_foot = 0.1
    total_cost = pool_volume * cost_per_cubic_foot
    result = total_cost
    return result

print(solution())