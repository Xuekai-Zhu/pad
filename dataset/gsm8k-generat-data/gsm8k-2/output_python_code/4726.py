def solution():
    """On March 1st the sun sets at 6 PM. Every day after the sun sets 1.2 minutes later. It is 6:10 PM and 40 days after March 1st. How many minutes until the sun sets?"""
    initial_set_time = 6 * 60
    daily_increase = 1.2
    time_elapsed = 40 * 10  # 10 minutes per day
    current_set_time = initial_set_time + time_elapsed
    time_until_set = (current_set_time - (6 * 60 + 10))  # time elapsed since 6:10pm
    result = time_until_set
    return result

print(solution())