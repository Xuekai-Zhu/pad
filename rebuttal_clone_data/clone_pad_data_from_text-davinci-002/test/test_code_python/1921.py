def solution():
    minutes_per_day = 30
    minutes_per_weekday = minutes_per_day
    minutes_per_saturday = minutes_per_weekday * 3
    minutes_per_week = minutes_per_weekday * 5 + minutes_per_saturday
    hours_per_week = minutes_per_week / 60
    result = hours_per_week
    return result

print(solution())