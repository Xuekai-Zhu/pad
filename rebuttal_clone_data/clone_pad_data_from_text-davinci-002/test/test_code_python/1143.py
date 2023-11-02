def solution():
    initial_books = 250
    books_taken_out = 120
    books_returned = 35
    books_withdrawn = 15
    books_in_library = initial_books - books_taken_out + books_returned - books_withdrawn
    result = books_in_library
    return result

print(solution())