def solution():
    
    laps_per_night = 5
    lap_distance = 100
    total_distance = laps_per_night * lap_distance
    feet_per_calorie = 25
    total_calories = (total_distance / feet_per_calorie) * 5
    result = total_calories
    return result

print(solution())