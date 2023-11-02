def solution():
    """Coral is reading a book that is 600 pages long. She reads half in the first week, and 30 percent of the remaining pages the second week. How many pages must she read the third week in order to finish the book?"""
    book_length = 600
    first_week = book_length / 2
    remaining_pages = book_length - first_week
    second_week = remaining_pages * 0.3
    third_week = book_length - first_week - second_week
    result = third_week
    return result

print(solution())