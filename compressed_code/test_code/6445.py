def solution():
    
    liters_per_week_per_cow = 108
    weeks = 5
    total_liters = 2160
    total_cows = (total_liters / (liters_per_week_per_cow * weeks)) * 6
    result = total_cows
    return result

print(solution())