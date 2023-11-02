def solution():
    """Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?"""
    # Define the total number of pages
    total_pages = 120

    # Define the number of pages Julie read yesterday and today
    yesterday_pages = 12
    today_pages = 2 * yesterday_pages

    # Calculate the total number of read pages
    read_pages = yesterday_pages + today_pages

    # Calculate the remaining pages
    remaining_pages = total_pages - read_pages

    # Calculate the number of pages Julie should read tomorrow
    tomorrow_pages = remaining_pages / 2

    result = tomorrow_pages
    return result

print(solution())