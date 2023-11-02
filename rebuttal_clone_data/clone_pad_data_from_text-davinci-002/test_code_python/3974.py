def solution():
    days_per_week = 7
    hours_per_day = 2
    pages_read_per_hour = 50
    total_pages = 2800
    days_to_read = total_pages / (hours_per_day * pages_read_per_hour)
    weeks_to_read = days_to_read / days_per_week
    result = weeks_to_read
    return result

print(solution())