def solution():
    """Justin needs to read at least 100 pages or more of his book in one week to pass his class. He has read 10 pages already on the first day. Assuming he reads twice the amount of pages as the first day each day in the remaining 6 days, how many pages will he have read after the week is over?"""
    total_pages = 100
    first_day_pages = 10
    days_left = 6
    multiplier = 2
    pages_read = first_day_pages
    for i in range(days_left):
        pages_read += (first_day_pages * multiplier**i)
    result = pages_read
    return result

print(solution())