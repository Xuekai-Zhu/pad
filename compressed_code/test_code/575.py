def solution():
    
    minutes_per_day = 45
    days_per_week = 4
    weeks = 2
    total_minutes = minutes_per_day * days_per_week * weeks
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())