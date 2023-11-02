def solution():
    
    liters_per_week = 108
    weeks = 5
    total_liters = 2160
    liters_per_cow_per_week = liters_per_week / 6
    total_cows = total_liters / (liters_per_cow_per_week * weeks)
    result = total_cows
    return result

print(solution())