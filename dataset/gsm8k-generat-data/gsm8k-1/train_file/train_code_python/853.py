def solution():
    """Jeff committed to run for an hour a day during weekdays. On Thursday, he cut short his run by 20 minutes but was able to jog 10 minutes more on Friday. How many minutes was he able to run for that week?"""
    daily_run_time = 60
    weekdays = 5
    thursday_reduction = 20
    friday_increase = 10
    total_run_time = daily_run_time * weekdays - thursday_reduction + friday_increase
    result = total_run_time
    return result

print(solution())