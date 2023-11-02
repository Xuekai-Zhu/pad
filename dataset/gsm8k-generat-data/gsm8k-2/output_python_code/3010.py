def solution():
    """Thomas is training at the gym to prepare for a competition. He trained for 5 hours every day for a month (30 days). If he continues to train for the next 12 days, how many hours will he spend on training in total?"""
    month_days = 30
    daily_hours = 5
    total_hours = month_days * daily_hours
    additional_days = 12
    additional_hours = additional_days * daily_hours
    total_training_hours = total_hours + additional_hours
    result = total_training_hours
    return result

print(solution())