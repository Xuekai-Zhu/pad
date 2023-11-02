def solution():
    """Every day Janet spends 8 minutes looking for her keys and another 3 minutes complaining after she finds them. If Janet stops losing her keys, how many minutes will she save every week?"""
    minutes_lost_per_day = 8 + 3
    days_per_week = 7
    minutes_saved_per_week = minutes_lost_per_day * days_per_week
    result = minutes_saved_per_week
    return result

print(solution())