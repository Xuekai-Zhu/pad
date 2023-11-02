def solution():
    """There are 336 books in a library. On Monday, 124 books are taken out. On Tuesday, 22 books are brought back. How many books are there now?"""
    # Define the initial number of books and the number taken and brought back
    initial_books = 336
    books_taken = 124
    books_brought_back = 22

    # Calculate the current number of books in the library
    current_books = initial_books - books_taken + books_brought_back

    # Display the current number of books
    result = current_books
    return result

print(solution())