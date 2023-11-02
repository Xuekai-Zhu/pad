def solution():
    """Thomas is training at the gym to prepare for a competition. He trained for 5 hours every day for a month (30 days). If he continues to train for the next 12 days, how many hours will he spend on training in total?"""
    # Define the number of hours Thomas trains per day and the total number of days
    HOURS_PER_DAY = 5
    TOTAL_DAYS = 30 + 12

    # Calculate the total number of hours Thomas trains
    total_hours = HOURS_PER_DAY * TOTAL_DAYS

    # Display the total number of hours Thomas trains
    result = total_hours
    return result

print(solution())