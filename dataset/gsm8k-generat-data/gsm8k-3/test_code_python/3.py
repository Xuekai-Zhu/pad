def solution():
    """Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?"""
    # Define the total number of pages in the book
    total_pages = 120

    # Define the number of pages Julie read yesterday and today
    pages_yesterday = 12
    pages_today = 2 * pages_yesterday

    # Calculate the number of remaining pages
    remaining_pages = total_pages - pages_yesterday - pages_today

    # Calculate the number of pages Julie should read tomorrow
    pages_tomorrow = remaining_pages / 2

    result = pages_tomorrow
    return result

print(solution())