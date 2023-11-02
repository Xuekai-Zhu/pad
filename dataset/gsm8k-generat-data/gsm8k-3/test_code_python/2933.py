def solution():
    """There are 235 books in a library. On Tuesday, 227 books are taken out. On Thursday, 56 books are brought back and 35 books are taken out again on Friday. How many books are there now?"""
    # Define the initial number of books in the library
    initial_books = 235

    # Calculate the number of books remaining after Tuesday
    books_remaining = initial_books - 227

    # Calculate the number of books remaining after Thursday
    books_remaining += 56

    # Calculate the number of books remaining after Friday
    books_remaining -= 35

    # Display the number of books remaining
    result = books_remaining
    return result

print(solution())