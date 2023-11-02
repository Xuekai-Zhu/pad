def solution():
    
    pool_length = 10
    pool_width = 8
    pool_depth = 6
    pool_volume = pool_length * pool_width * pool_depth
    chlorine_ratio = 120
    chlorine_needed = pool_volume / chlorine_ratio
    chlorine_price = 3
    total_cost = chlorine_price * chlorine_needed
    result = total_cost
    return result

print(solution())