def solution():
    """There are 235 books in a library. On Tuesday, 227 books are taken out. On Thursday, 56 books are brought back and 35 books are taken out again on Friday. How many books are there now?"""
    initial_books = 235
    tuesday_books = 227
    thursday_books = -56
    friday_books = -35
    total_books = initial_books + tuesday_books + thursday_books + friday_books
    result = total_books
    return result

print(solution())