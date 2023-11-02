def solution():
    """Tom reads 10 hours over 5 days. He can read 50 pages per hour. Assuming he reads the same amount every day how many pages does he read in 7 days?"""
    total_hours = 10
    pages_per_hour = 50
    days = 5
    pages_per_day = total_hours * pages_per_hour / days
    pages_in_7_days = pages_per_day * 7
    result = pages_in_7_days
    return result

print(solution())