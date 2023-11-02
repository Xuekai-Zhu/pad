def solution():
    """There are 235 books in a library. On Tuesday, 227 books are taken out. On Thursday, 56 books are brought back and 35 books are taken out again on Friday. How many books are there now?"""
    # Define the initial number of books
    initial_books = 235

    # Subtract the books taken out on Tuesday
    remaining_books = initial_books - 227

    # Add the books brought back on Thursday
    remaining_books += 56

    # Subtract the books taken out again on Friday
    remaining_books -= 35

    # return the result
    result = remaining_books
    return result

print(solution())