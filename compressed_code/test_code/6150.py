def solution():
    
    laps_per_day = 5
    lap_distance = 100
    total_distance = laps_per_day * lap_distance
    calories_per_foot = 1 / 25
    calories_burned = total_distance * calories_per_foot
    total_days = 5
    total_calories_burned = calories_burned * total_days
    result = total_calories_burned
    return result

print(solution())