def solution():
    """Solo has to read 4 pages from his Science textbook, 20 pages from his Social Studies textbook, 7 pages from his History textbook and 8 pages from his Geography textbook. Solo read 15 pages on Monday. If he has 4 more days to complete all his reading, how many pages does he need to read, on average, in one day?"""
    total_pages = 4 + 20 + 7 + 8
    pages_left = total_pages - 15
    days_left = 4
    pages_per_day = pages_left / days_left
    result = pages_per_day
    return result

print(solution())