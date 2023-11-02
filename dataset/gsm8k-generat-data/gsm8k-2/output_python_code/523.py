def solution():
    """There are 336 books in a library. On Monday, 124 books are taken out. On Tuesday, 22 books are brought back. How many books are there now?"""
    total_books = 336
    monday_books = 124
    tuesday_books = 22
    remaining_books = total_books - monday_books + tuesday_books
    result = remaining_books
    return result

print(solution())