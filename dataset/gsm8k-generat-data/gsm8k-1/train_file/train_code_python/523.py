def solution():
    """There are 336 books in a library. On Monday, 124 books are taken out. On Tuesday, 22 books are brought back. How many books are there now?"""
    initial_books = 336
    monday_books_out = 124
    tuesday_books_in = 22
    remaining_books = initial_books - monday_books_out + tuesday_books_in
    result = remaining_books
    return result

print(solution())