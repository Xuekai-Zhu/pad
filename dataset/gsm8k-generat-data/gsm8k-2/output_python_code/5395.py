def solution():
    """Justin needs to read at least 100 pages or more of his book in one week to pass his class. He has read 10 pages already on the first day. Assuming he reads twice the amount of pages as the first day each day in the remaining 6 days, how many pages will he have read after the week is over?"""
    target_pages = 100
    first_day_pages = 10
    remaining_days = 6
    daily_multiplier = 2
    total_pages = first_day_pages + \
        (daily_multiplier**(remaining_days)) * first_day_pages
    result = total_pages
    return result

print(solution())