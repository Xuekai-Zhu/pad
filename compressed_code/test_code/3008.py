def solution():
    
    ideal_weekday_hours = 8
    ideal_weekend_hours = 8
    actual_weekday_hours = 5
    actual_weekend_hours = 6
    weekday_difference = ideal_weekday_hours - actual_weekday_hours
    weekend_difference = ideal_weekend_hours - actual_weekend_hours
    total_weekday_hours = weekday_difference * 5
    total_weekend_hours = weekend_difference * 2
    total_difference = total_weekday_hours + total_weekend_hours
    result = total_difference
    return result

print(solution())