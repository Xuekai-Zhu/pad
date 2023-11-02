def solution():
    """Coral is reading a book that is 600 pages long. She reads half of it in the first week, and 30 percent of the remaining pages the second week. How many pages must she read the third week in order to finish the book?"""
    book_size = 600
    first_week = book_size / 2
    remaining_pages = book_size - first_week
    second_week = 0.3 * remaining_pages
    pages_left = book_size - first_week - second_week
    result = pages_left / 1  # assuming she reads equally in the third week
    return result

print(solution())