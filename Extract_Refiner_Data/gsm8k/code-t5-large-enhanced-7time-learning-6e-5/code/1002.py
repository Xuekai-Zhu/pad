def solution():
    
    pool_width = 14
    pool_length = 25
    pool_depth = 4
    pool_volume = pool_width * pool_length * pool_depth
    pool_gallons = pool_volume / 5.9
    cost_per_gallon = 0.10
    total_cost = pool_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())