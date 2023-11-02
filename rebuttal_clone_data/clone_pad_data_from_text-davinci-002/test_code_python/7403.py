def solution():
    days_per_week = 7
    days_off = 2
    hours_per_day = 4
    hours_per_week = (days_per_week - days_off) * hours_per_day
    weeks_per_year = 52
    hours_per_year = hours_per_week * weeks_per_year
    result = hours_per_year
    return result

print(solution())