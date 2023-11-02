def solution():
    
    pool_depth = 10
    pool_width = 6
    pool_length = 20
    cubic_feet = pool_depth * pool_width * pool_length
    liters = cubic_feet * 25
    cost_per_liter = 3
    total_cost = liters * cost_per_liter
    result = total_cost
    return result

print(solution())