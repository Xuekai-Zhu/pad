def solution():
    """Lance wants to finish reading a 100 page book in 3 days. Yesterday, he started to read 35 pages. Today, he read 5 fewer pages than yesterday. How many pages should he read tomorrow to finish the book?"""
    total_pages = 100
    days_left = 3 - 2    # Today is the second day
    pages_read_yesterday = 35
    pages_read_today = pages_read_yesterday - 5
    pages_left = total_pages - pages_read_yesterday - pages_read_today
    pages_to_read_tomorrow = pages_left / days_left
    result = pages_to_read_tomorrow
    return result

print(solution())