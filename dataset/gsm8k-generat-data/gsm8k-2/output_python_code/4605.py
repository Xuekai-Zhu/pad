def solution():
    """Nate is reading a 400-page book. He finished reading 20% of the book. How many pages does he need to read to finish the book?"""
    book_pages = 400
    finished_percent = 0.2
    finished_pages = finished_percent * book_pages
    remaining_pages = book_pages - finished_pages
    result = remaining_pages
    return result

print(solution())