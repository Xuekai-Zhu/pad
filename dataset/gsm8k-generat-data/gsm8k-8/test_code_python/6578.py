def solution():
    # Define the initial number of books
    initial_books = 9900

    # Calculate the number of books that are left
    books_left = initial_books * (4/6)

    # Calculate the number of books that were sold
    books_sold = initial_books - books_left
    result = books_sold
    return result

print(solution())