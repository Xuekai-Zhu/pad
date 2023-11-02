def solution():
    """James trains for the Olympics. He trains twice a day for 4 hours each time for all but 2 days per week. How many hours does he train a year?"""
    days_per_week = 7
    training_days_per_week = 5
    training_sessions_per_day = 2
    hours_per_session = 4
    weeks_per_year = 52
    training_hours_per_week = training_days_per_week * training_sessions_per_day * hours_per_session
    total_training_hours = training_hours_per_week * (weeks_per_year - (days_per_week - training_days_per_week))
    result = total_training_hours
    return result

print(solution())