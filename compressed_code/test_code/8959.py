def solution():
    
    minutes_per_session = 30
    sessions_per_day = 2
    minutes_per_hour = 60
    days_per_week = 7
    total_minutes = minutes_per_session * sessions_per_day * days_per_week
    total_hours = total_minutes / minutes_per_hour
    result = total_hours
    return result

print(solution())