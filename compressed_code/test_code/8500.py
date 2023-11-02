def solution():
    
    weekday_minutes = 30
    saturday_minutes = weekday_minutes * 3
    total_weekday_minutes = weekday_minutes * 5
    total_saturday_minutes = saturday_minutes
    total_minutes = total_weekday_minutes + total_saturday_minutes
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())