def solution():
    
    
    
    earrings_day1 = 3
    earrings_day2 = 2 * earrings_day1
    earrings_day3 = earrings_day2 - 1
    
    
    gumballs_day1 = 9 * earrings_day1
    gumballs_day2 = 9 * earrings_day2
    gumballs_day3 = 9 * earrings_day3
    
    
    total_gumballs = gumballs_day1 + gumballs_day2 + gumballs_day3
    
    
    gumballs_per_day = 3
    days = total_gumballs // gumballs_per_day
    
    result = days
    return result

print(solution())