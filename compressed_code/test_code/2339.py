def solution():
    
    month_days = 30
    daily_hours = 5
    total_hours = month_days * daily_hours
    additional_days = 12
    additional_hours = additional_days * daily_hours
    total_training_hours = total_hours + additional_hours
    result = total_training_hours
    return result

print(solution())