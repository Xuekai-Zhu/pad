def solution():
    hours_per_day = 5
    training_days = 30
    additional_days = 12

    total_training_days = training_days + additional_days
    total_training_hours = total_training_days * hours_per_day
    result = total_training_hours
    return result

print(solution())