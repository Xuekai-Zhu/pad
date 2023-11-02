def solution():
    
    ideal_weekday_hours = 8
    ideal_weekend_hours = 8
    actual_weekday_hours = 5
    actual_weekend_hours = 6
    weekday_hours_behind = ideal_weekday_hours - actual_weekday_hours
    weekend_hours_behind = ideal_weekend_hours - actual_weekend_hours
    total_hours_behind = (weekday_hours_behind * 5) + (weekend_hours_behind * 2)
    result = total_hours_behind
    return result

print(solution())