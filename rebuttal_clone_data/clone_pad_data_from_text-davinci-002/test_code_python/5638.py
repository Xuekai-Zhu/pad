def solution():
    hours_per_weekday = 7
    hours_per_weekend = 8
    days_in_week = 7
    hours_slept_weekdays = hours_per_weekday * 5
    hours_slept_weekends = hours_per_weekend * 2
    hours_slept_per_week = hours_slept_weekdays + hours_slept_weekends
    result = hours_slept_per_week
    return result

print(solution())