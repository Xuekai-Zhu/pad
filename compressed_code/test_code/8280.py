def solution():
    
    pies_per_day = 3
    days_baked = 11
    total_pies = pies_per_day * days_baked
    pies_eaten = 4
    pies_left = total_pies - pies_eaten
    whipped_cream_per_pie = 2
    cans_needed = pies_left * whipped_cream_per_pie
    result = cans_needed
    return result

print(solution())