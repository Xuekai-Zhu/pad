def solution():
    """Ethan is reading a sci-fi book that has 360 pages. He read 40 pages on Saturday morning and another 10 pages at night. The next day he read twice the total pages as on Saturday. How many pages does he have left to read?"""
    total_pages = 360
    saturday_pages = 40 + 10
    sunday_pages = 2 * saturday_pages
    pages_read = saturday_pages + sunday_pages
    pages_left = total_pages - pages_read
    result = pages_left
    return result

print(solution())