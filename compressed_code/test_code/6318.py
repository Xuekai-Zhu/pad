def solution():
    
    nights_per_week = 5
    hours_per_night = 2
    weekend_hours = 3 * 2
    total_weekend_hours = weekend_hours * 6
    total_week_hours = nights_per_week * hours_per_night
    total_hours = total_week_hours * 6 + total_weekend_hours
    result = total_hours
    return result

print(solution())