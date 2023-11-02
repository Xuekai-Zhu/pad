def solution():
    days_per_week = 7
    hours_day_one = 2
    hours_day_two = 3
    total_hours = hours_day_one + (hours_day_two * (days_per_week - 1))
    result = total_hours
    return result

print(solution())