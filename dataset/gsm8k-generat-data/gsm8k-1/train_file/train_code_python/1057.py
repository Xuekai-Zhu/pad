def solution():
    """Tom reads 10 hours over 5 days. He can read 50 pages per hour. Assuming he reads the same amount every day how many pages does he read in 7 days?"""
    hours_per_day = 2
    days_read = 5
    total_hours_read = hours_per_day * days_read
    pages_per_hour = 50
    pages_read = total_hours_read * pages_per_hour
    pages_read_per_week = pages_read * 7 / 5
    result = pages_read_per_week
    return result

print(solution())