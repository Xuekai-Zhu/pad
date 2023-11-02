def solution():
    minutes_per_day = 45
    minutes_per_hour = 60
    hours_per_day = minutes_per_day / minutes_per_hour
    days_allowed_per_week = 4
    days_in_two_weeks = 14
    total_hours = hours_per_day * days_allowed_per_week * days_in_two_weeks
    result = total_hours
    return result

print(solution())