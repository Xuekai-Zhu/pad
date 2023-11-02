def solution():
    """There are 250 books inside a library. On Tuesday, 120 books are taken out to be read by children. On Wednesday, 35 books are returned. On Thursday, another 15 books are withdrawn from the library. How many books are now in the library?"""
    initial_books = 250
    books_taken_tuesday = 120
    books_returned_wednesday = 35
    books_taken_thursday = 15
    total_books = initial_books - books_taken_tuesday + books_returned_wednesday - books_taken_thursday
    result = total_books
    return result

print(solution())