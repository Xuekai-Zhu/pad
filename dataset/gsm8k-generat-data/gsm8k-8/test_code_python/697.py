def solution():
    # Calculate the time Joey spends studying on weekdays
    weekday_time = 2 * 5

    # Calculate the time Joey spends studying on weekends
    weekend_time = 3 * 2

    # Calculate the total time Joey spends studying in one week
    weekly_time = weekday_time + weekend_time

    # Calculate the total time Joey spends studying for 6 weeks
    total_time = weekly_time * 6

    result = total_time
    return result

print(solution())