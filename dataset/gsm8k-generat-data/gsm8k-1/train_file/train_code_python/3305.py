def solution():
    """Larry jogs for 30 minutes each day. In the first week, he jogs for 3 days while he jogs for 5 days in the second week. How many hours does he jog in total for two weeks?"""
    minutes_per_day = 30
    days_first_week = 3
    days_second_week = 5
    total_minutes = (minutes_per_day * days_first_week) + (minutes_per_day * days_second_week)
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())