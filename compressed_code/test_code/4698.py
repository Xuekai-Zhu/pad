def solution():
    
    shampoo_daily = 1
    conditioner_daily = 0.5 * shampoo_daily
    total_days = 14
    total_shampoo = shampoo_daily * total_days
    total_conditioner = conditioner_daily * total_days
    result = total_shampoo + total_conditioner
    return result

print(solution())