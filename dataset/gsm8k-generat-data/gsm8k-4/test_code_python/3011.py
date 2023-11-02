def solution():
    """Thomas is training at the gym to prepare for a competition. He trained for 5 hours every day for a month (30 days). If he continues to train for the next 12 days, how many hours will he spend on training in total?"""
    # Define the number of hours Thomas trains per day and the number of days he trains
    hours_per_day = 5
    days = 42    # 30 + 12

    # Calculate the total number of hours Thomas will spend on training
    total_hours = hours_per_day * days

    result = total_hours
    return result

print(solution())