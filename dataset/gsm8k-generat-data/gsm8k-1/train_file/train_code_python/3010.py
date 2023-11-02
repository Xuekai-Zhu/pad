def solution():
    """Thomas is training at the gym to prepare for a competition. He trained for 5 hours every day for a month (30 days). If he continues to train for the next 12 days, how many hours will he spend on training in total?"""
    hours_per_day = 5
    days_in_month = 30
    total_hours_month = hours_per_day * days_in_month
    additional_days = 12
    total_hours = total_hours_month + (additional_days * hours_per_day)
    result = total_hours
    return result

print(solution())