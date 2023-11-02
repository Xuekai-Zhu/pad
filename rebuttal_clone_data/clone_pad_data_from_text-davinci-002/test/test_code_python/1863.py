def solution():
    minutes_per_day = 30
    minutes_per_hour = 60
    days_first_week = 3
    hours_first_week= minutes_per_day * days_first_week / minutes_per_hour
    days_second_week = 5
    hours_second_week = minutes_per_day * days_second_week / minutes_per_hour
    total_hours = hours_first_week + hours_second_week
    result = total_hours
    return result

print(solution())