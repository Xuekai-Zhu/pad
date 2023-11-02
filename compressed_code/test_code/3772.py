def solution():
    
    daily_water_consumption = 72
    weekly_water_consumption = daily_water_consumption * 7
    bottle_size = 84
    fill_times_per_week = weekly_water_consumption // bottle_size
    result = fill_times_per_week
    return result

print(solution())