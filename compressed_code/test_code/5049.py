def solution():
    
    bike_cost = 112
    days_to_sell = 14
    total_bracelets_needed = bike_cost
    bracelets_per_day = total_bracelets_needed / (days_to_sell * 1.0)
    result = bracelets_per_day
    return result

print(solution())