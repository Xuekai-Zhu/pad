def solution():
    """John writes 20 pages a day. How long will it take him to write 3 books that are 400 pages each?"""
    pages_per_day = 20
    pages_per_book = 400
    num_books = 3
    total_pages = pages_per_book * num_books
    days_to_write = total_pages // pages_per_day
    result = days_to_write
    return result

print(solution())