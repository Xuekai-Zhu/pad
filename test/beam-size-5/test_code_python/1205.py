def solution():
    
    low_setting_water_per_day = 1
    medium_setting_water_per_day = low_setting_water_per_day * 2
    high_setting_water_per_day = medium_setting_water_per_day * 2
    total_water_removed_per_day = low_setting_water_per_day + medium_setting_water_per_day + high_setting_water_per_day
    total_water_removed = total_water_removed_per_day * 3
    result = total_water_removed
    return result

print(solution())