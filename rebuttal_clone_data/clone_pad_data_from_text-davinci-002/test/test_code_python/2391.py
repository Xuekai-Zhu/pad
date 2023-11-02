def solution():
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_per_day = 2
    days_per_week = 7
    beats_per_week = beats_per_minute * minutes_per_hour * hours_per_day * days_per_week
    result = beats_per_week
    return result

print(solution())