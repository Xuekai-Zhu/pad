def solution():
    """Larry jogs for 30 minutes each day. In the first week, he jogs for 3 days while he jogs for 5 days in the second week. How many hours does he jog in total for two weeks?"""
    total_days = 3 + 5
    total_jogging_time = total_days * 30
    total_jogging_hours = total_jogging_time / 60
    result = total_jogging_hours
    return result

print(solution())