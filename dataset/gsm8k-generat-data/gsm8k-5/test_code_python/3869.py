def solution():
    # Calculate the total amount of sleep Tom should have gotten in the last week
    ideal_weekly_sleep = (5 * 8) + (2 * 6 * 8)  # 5 weeknights * 8 hours + 2 weekends * 6 hours/night * 8 nights

    # Calculate the actual amount of sleep Tom got in the last week
    actual_weekly_sleep = (5 * 5) + (2 * 6)  # 5 weeknights * 5 hours/night + 2 weekends * 6 hours/night

    # Calculate the difference between the ideal and actual amounts of sleep
    sleep_deficit = ideal_weekly_sleep - actual_weekly_sleep
    result = sleep_deficit
    return result

print(solution())