def solution():
    """Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?"""
    total_pages = 120
    yesterday_pages = 12
    today_pages = 2 * yesterday_pages
    remaining_pages = total_pages - yesterday_pages - today_pages
    half_remaining_pages = remaining_pages / 2
    pages_to_read_tomorrow = half_remaining_pages
    result = pages_to_read_tomorrow
    return result

print(solution())