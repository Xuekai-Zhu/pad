def solution():
    daily_sports_time = 2
    num_days_per_week = 5
    num_missed_days = 2

    # Calculate the total number of days Roy went to school that week
    total_days = num_days_per_week - num_missed_days

    # Calculate the total time Roy spent on sports activities in school that week
    total_sports_time = daily_sports_time * total_days
    result = total_sports_time
    return result

print(solution())