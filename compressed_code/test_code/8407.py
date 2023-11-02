def solution():
    
    tea_per_day = 1/5
    ounces_per_box = 28
    cups_per_box = ounces_per_box / tea_per_day
    weeks_per_box = cups_per_box / 7
    result = weeks_per_box
    return result

print(solution())