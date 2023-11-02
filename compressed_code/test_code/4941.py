def solution():
    
    num_horses = 8
    drinking_water_per_day = 5
    bathing_water_per_day = 2
    total_water_per_day = (drinking_water_per_day + bathing_water_per_day) * num_horses
    total_water_for_28_days = total_water_per_day * 28
    result = total_water_for_28_days
    return result

print(solution())