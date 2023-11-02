def solution():
    """Mr. John jogs for 1 hour 30 minutes in the morning every day. How much time (in hours) will he have spent jogging after two weeks?"""
    jog_time_per_day = 1.5 # in hours
    days_per_week = 7
    weeks = 2
    total_jog_time = jog_time_per_day * days_per_week * weeks
    result = total_jog_time
    return result

print(solution())