def solution():
    """There are 336 books in a library. On Monday, 124 books are taken out. On Tuesday, 22 books are brought back. How many books are there now?"""
    # Define the initial number of books and the number of books taken out and brought back
    initial_books = 336
    books_taken_out = 124
    books_brought_back = 22

    # Calculate the number of books currently in the library
    current_books = initial_books - books_taken_out + books_brought_back

    # return the result
    result = current_books
    return result

print(solution())