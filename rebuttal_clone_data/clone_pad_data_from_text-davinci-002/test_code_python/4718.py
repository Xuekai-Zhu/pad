def solution():
    pages_written_per_hour = 5
    total_pages = 735
    hours_written_per_day = 3
    days_written_per_week = 5
    pages_written_per_day = hours_written_per_day * pages_written_per_hour
    weeks_to_finish = total_pages / pages_written_per_day
    result = weeks_to_finish
    return result

print(solution())