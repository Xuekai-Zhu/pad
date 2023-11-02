def solution():
    
    total_distance = 60
    days_per_week = 3
    first_day_hours = 3
    second_day_hours = first_day_hours / 2
    total_hours = (first_day_hours * days_per_week) + (second_day_hours * days_per_week)
    fast_speed = total_distance / total_hours
    result = fast_speed
    return result

print(solution())