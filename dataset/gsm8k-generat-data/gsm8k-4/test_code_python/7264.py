def solution():
    """The capacity of Karson's home library is 400 books. If he currently has 120 books, how many more books does he have to buy to make his library 90% full?"""
    # Define the capacity of the library
    library_capacity = 400

    # Define the current number of books
    current_books = 120

    # Calculate the number of books needed to reach 90% capacity
    books_needed = int(library_capacity * 0.9 - current_books)

    result = books_needed
    return result

print(solution())