def solution():
    
    days_per_week = 7
    training_days_per_week = days_per_week - 2
    hours_per_training = 4 * 2
    total_training_hours_per_week = hours_per_training * training_days_per_week
    weeks_per_year = 52
    total_training_hours_per_year = total_training_hours_per_week * weeks_per_year
    result = total_training_hours_per_year
    return result

print(solution())