def solution():
    hours_slept_per_weekday = 6
    hours_slept_per_weekend = 9
    hours_slept_per_weekend_with_nap = 10
    days_in_week = 7
    weeks_in_month = 4
    days_slept_per_weekday = days_in_week * weeks_in_month
    days_slept_per_weekend = days_in_week * 2
    total_hours_slept = (hours_slept_per_weekday * days_slept_per_weekday) + (hours_slept_per_weekend_with_nap * days_slept_per_weekend)
    result = total_hours_slept
    return result

print(solution())