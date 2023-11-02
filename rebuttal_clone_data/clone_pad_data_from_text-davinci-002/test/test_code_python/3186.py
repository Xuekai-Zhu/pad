def solution():
    pages_read_per_day = 100
    pages_in_book = 2100
    days_in_week = 7
    pages_read_per_week = pages_read_per_day * 3
    weeks_to_read = pages_in_book / pages_read_per_week
    result = weeks_to_read
    return result

print(solution())