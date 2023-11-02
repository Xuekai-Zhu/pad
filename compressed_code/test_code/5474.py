def solution():
    
    initial_snow = 0.5
    second_day_snow = 8 / 12  
    melted_snow = 2 / 12  
    total_snow_after_three_days = initial_snow + second_day_snow - melted_snow
    fifth_day_snow = 2 * initial_snow
    total_snow = total_snow_after_three_days + fifth_day_snow
    result = total_snow
    return result

print(solution())