def solution():
    
    days_per_week = 3
    weightlifting_hours_per_day = 1
    cardio_hours_per_day = weightlifting_hours_per_day / 3
    total_hours_per_day = weightlifting_hours_per_day + cardio_hours_per_day
    total_hours = total_hours_per_day * days_per_week
    result = total_hours
    return result

print(solution())