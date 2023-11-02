def solution():
    daily_reading_time = 2
    extra_reading_time = 4
    num_days_in_week = 7

    # Calculate the total time Mark currently spends on reading books in a week
    current_weekly_reading_time = daily_reading_time * num_days_in_week

    # Calculate the total time Mark wants to spend on reading books in a week after increasing his time by 4 hours
    desired_weekly_reading_time = current_weekly_reading_time + extra_reading_time
    result = desired_weekly_reading_time
    return result

print(solution())