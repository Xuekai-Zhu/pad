def solution():
    total_pages = 500
    pages_read_per_day = 10
    pages_read_per_day_2 = 5
    days = total_pages / pages_read_per_day
    days_2 = (total_pages / 2) / pages_read_per_day_2
    result = days + days_2
    return result

print(solution())