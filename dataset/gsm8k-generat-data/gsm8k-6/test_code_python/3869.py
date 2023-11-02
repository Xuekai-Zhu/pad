def solution():
    # Calculate the total number of hours Tom would ideally like to sleep in a week
    ideal_weekly_sleep = 8*5 + 8*2  # 8 hours of sleep on weekdays and weekends
    # Calculate the actual number of hours Tom slept in the last week
    actual_weekly_sleep = 5*5 + 2*6  # 5 hours on weeknights and 6 hours on weekends
    # Calculate the number of hours Tom is behind on from the last week
    sleep_deficit = ideal_weekly_sleep - actual_weekly_sleep
    result = sleep_deficit
    return result

print(solution())