def solution():
    hours_per_day = 2
    days_per_week = 5
    hours_per_week = hours_per_day * days_per_week
    missed_days = 2
    hours_missed = hours_per_day * missed_days
    total_hours = hours_per_week - hours_missed
    result = total_hours
    return result

print(solution())