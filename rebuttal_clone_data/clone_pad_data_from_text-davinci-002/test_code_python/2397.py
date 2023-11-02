def solution():
    nathan_hours_per_day = 3
    nathan_days_per_week = 2
    tobias_hours_per_day = 5
    tobias_days_per_week = 1
    nathan_total_hours = nathan_hours_per_day * nathan_days_per_week * 2
    tobias_total_hours = tobias_hours_per_day * tobias_days_per_week
    total_hours = nathan_total_hours + tobias_total_hours
    result = total_hours
    return result

print(solution())