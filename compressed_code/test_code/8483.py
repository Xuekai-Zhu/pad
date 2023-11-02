def solution():
    
    soda_needed = 80
    can_size = 8
    price_per_can = 0.5
    cans_needed = soda_needed / can_size
    total_cost = cans_needed * price_per_can
    result = total_cost
    return result

print(solution())