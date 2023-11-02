def solution():
    
    morning_water = 4
    evening_water = 6
    total_water_per_day = morning_water + evening_water
    total_water_needed = 50
    days_to_reach_total = total_water_needed / total_water_per_day
    result = days_to_reach_total
    return result

print(solution())