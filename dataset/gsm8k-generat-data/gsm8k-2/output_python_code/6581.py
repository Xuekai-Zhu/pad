def solution():
    """A new edition Geometry book has 450 pages which are 230 pages less than twice as many pages as the old edition. How many pages did the old edition Geometry book have?"""
    new_book_pages = 450
    old_book_pages = (new_book_pages + 230) / 2
    result = old_book_pages
    return result

print(solution())