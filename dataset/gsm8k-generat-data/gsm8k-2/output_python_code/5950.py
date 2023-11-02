def solution():
    """Cora started reading a 158-page book on Monday, and she decided she wanted to finish it by the end of Friday. She read 23 pages on Monday, 38 pages on Tuesday, and 61 pages on Wednesday. She knows she will have time to read twice as much on Friday as she does on Thursday. How many pages does she have to read on Thursday to finish the book in time?"""
    total_pages = 158
    read_so_far = 23 + 38 + 61
    remaining_pages = total_pages - read_so_far
    days_left = 2  # Thursday and Friday
    pages_left_per_day = remaining_pages / days_left
    pages_to_read_on_thursday = pages_left_per_day / 3  # Friday = 2 * Thursday
    result = pages_to_read_on_thursday
    return result

print(solution())