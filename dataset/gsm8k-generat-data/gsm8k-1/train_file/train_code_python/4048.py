def solution():
    """Ethan is reading a sci-fi book that has 360 pages. He read 40 pages on Saturday morning and another 10 pages at night. The next day he read twice the total pages as on Saturday. How many pages does he have left to read?"""
    total_pages = 360
    pages_read_saturday = 40 + 10
    pages_read_sunday = 2 * pages_read_saturday
    pages_left = total_pages - pages_read_saturday - pages_read_sunday
    result = pages_left
    return result

print(solution())