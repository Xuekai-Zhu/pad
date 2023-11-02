def solution():
    hours_per_day = 6  # Tim spends 6 hours each day at work
    minutes_per_call = 15  # It takes Tim 15 minutes to deal with a call
    days_per_week = 5  # Tim works 5 days in a week

    # Calculate the total number of calls Tim deals in a week
    total_calls = hours_per_day * minutes_per_call * days_per_week
    result = total_calls
    return result

print(solution())