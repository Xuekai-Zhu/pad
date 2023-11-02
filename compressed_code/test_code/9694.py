def solution():
    
    morning_liters = 4
    evening_liters = 6
    total_liters_per_day = morning_liters + evening_liters
    days_to_reach_50_liters = 50 / total_liters_per_day
    result = days_to_reach_50_liters
    return result

print(solution())