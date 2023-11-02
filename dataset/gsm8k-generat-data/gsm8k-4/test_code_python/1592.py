def solution():
    """Betty has 20 books, and her sister has 1/4 times more books than Betty. What's the total number of books the two have?"""
    # Define the initial number of books
    betty_books = 20

    # Calculate the number of books the sister has
    sister_books = betty_books * (1 + 1/4)

    # Calculate the total number of books
    total_books = betty_books + sister_books

    result = total_books
    return result

print(solution())