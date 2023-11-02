def solution():
    total_pages = 120  # Julie is reading a 120-page book
    pages_read_yesterday = 12  # Julie read 12 pages yesterday
    pages_read_today = 2 * pages_read_yesterday  # Julie read twice as many pages today
    pages_left = total_pages - pages_read_yesterday - pages_read_today  # Julie has this many pages left
    pages_to_read_tomorrow = pages_left / 2  # Julie wants to read half of the remaining pages tomorrow
    result = pages_to_read_tomorrow
    return result

print(solution())