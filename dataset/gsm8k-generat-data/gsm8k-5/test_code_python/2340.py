def solution():
    # Number of books Jamal shelve in each section
    history_books = 12
    fiction_books = 19
    childrens_books = 8

    # Number of books on the cart before adding misplaced books
    initial_books = history_books + fiction_books + childrens_books

    # Number of misplaced books added to the cart
    misplaced_books = 4

    # Number of books Jamal still has to shelve
    remaining_books = 16

    # Number of books on the cart initially
    total_books = initial_books + misplaced_books + remaining_books
    result = total_books
    return result

print(solution())