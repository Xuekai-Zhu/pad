def solution():
    
    weekday_minutes = 30 * 5 
    weekend_hours = 2 
    total_weekend_minutes = weekend_hours * 60 
    total_minutes_per_week = weekday_minutes + total_weekend_minutes
    total_minutes_per_year = total_minutes_per_week * 52
    total_hours_per_year = total_minutes_per_year / 60
    result = total_hours_per_year
    return result

print(solution())