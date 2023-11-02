def solution():
    total_pages = 500  # Cyrus has to write a 500 page book
    pages_day1 = 25  # Cyrus writes 25 pages on the first day
    pages_day2 = 2 * pages_day1  # Cyrus writes twice as many pages on the second day
    pages_day3 = 2 * pages_day2  # Cyrus writes twice as many pages on the third day
    pages_day4 = 10  # Cyrus writes only 10 pages on the fourth day

    # Calculate the total number of pages Cyrus has written so far
    total_pages_written = pages_day1 + pages_day2 + pages_day3 + pages_day4

    # Calculate the number of remaining pages
    remaining_pages = total_pages - total_pages_written
    result = remaining_pages
    return result

print(solution())