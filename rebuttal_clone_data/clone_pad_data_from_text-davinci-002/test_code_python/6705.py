def solution():
    hours_read_per_day = 2
    percent_increase = 150
    increased_hours_read = hours_read_per_day * (1 + (percent_increase / 100))
    pages_read_per_day = 100
    pages_read_per_week = increased_hours_read * pages_read_per_day
    result = pages_read_per_week
    return result

print(solution())