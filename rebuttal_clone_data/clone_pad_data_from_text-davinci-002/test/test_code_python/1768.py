def solution():
    pool_size = 10 * 6 * 20
    liter_price = 3
    liters_per_cubic_foot = 25
    total_liters = pool_size * liters_per_cubic_foot
    total_price = total_liters * liter_price
    result = total_price
    
    return result

print(solution())