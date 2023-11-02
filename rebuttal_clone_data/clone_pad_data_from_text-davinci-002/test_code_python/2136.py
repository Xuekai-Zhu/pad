def solution():
    hours_needed = 50
    minutes_per_day = 20
    minutes_per_hour = 60
    hours_per_day = hours_needed / minutes_per_hour
    days_needed = hours_per_day / minutes_per_day
    result = days_needed
    return result

print(solution())