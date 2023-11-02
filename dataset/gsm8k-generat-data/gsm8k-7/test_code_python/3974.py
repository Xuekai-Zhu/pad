def solution():
    reading_time_per_day = 2  # hours
    reading_rate = 50  # pages per hour
    total_pages = 2800
    pages_per_week = reading_time_per_day * 7 * reading_rate
    weeks_to_finish = total_pages / pages_per_week
    result = weeks_to_finish
    return result

print(solution())