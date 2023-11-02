def solution():
    
    pies_per_day = 3
    total_days = 11
    total_pies = pies_per_day * total_days
    whipped_cream_per_pie = 2
    eaten_pies = 4
    remaining_pies = total_pies - eaten_pies
    total_whipped_cream = remaining_pies * whipped_cream_per_pie
    result = total_whipped_cream
    return result

print(solution())