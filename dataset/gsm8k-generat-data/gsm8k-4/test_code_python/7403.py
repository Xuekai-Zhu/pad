def solution():
    """James trains for the Olympics. He trains twice a day for 4 hours each time for all but 2 days per week. How many hours does he train a year?"""
    # Define the number of training hours per day and the number of training days per week
    TRAINING_HOURS_PER_DAY = 8
    TRAINING_DAYS_PER_WEEK = 5

    # Calculate the number of training hours per week
    weekly_training_hours = TRAINING_HOURS_PER_DAY * TRAINING_DAYS_PER_WEEK

    # Calculate the number of training hours per year, accounting for the 2 rest days per week
    yearly_training_hours = weekly_training_hours * 50

    # Return the result
    result = yearly_training_hours
    return result

print(solution())