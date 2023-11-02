def solution():
    hours_per_day = 10/5  # Tom reads for 2 hours every day for 5 days
    pages_per_hour = 50  # Tom can read 50 pages per hour
    pages_per_day = hours_per_day * pages_per_hour  # Tom can read this many pages in one day
    pages_in_7_days = pages_per_day * 7  # Tom reads this many pages in 7 days
    result = pages_in_7_days
    return result

print(solution())