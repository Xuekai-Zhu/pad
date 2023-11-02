def solution():
    """Jeff committed to run for an hour a day during weekdays. On Thursday, he cut short his run by 20 minutes but was able to jog 10 minutes more on Friday. How many minutes was he able to run for that week?"""
    time_per_day = 60
    total_time = 5 * time_per_day
    thursday_time = time_per_day - 20
    friday_time = time_per_day + 10
    total_time += thursday_time + friday_time
    result = total_time
    return result

print(solution())