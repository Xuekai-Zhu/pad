def solution():
    
    original_days = 3
    extra_days = 2
    morning_hours = 1
    evening_hours = 1
    total_days = original_days + extra_days
    total_hours_per_day = morning_hours + evening_hours
    total_hours = total_days * total_hours_per_day
    result = total_hours
    return result

print(solution())