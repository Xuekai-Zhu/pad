def solution():
    """The capacity of Karson's home library is 400 books. If he currently has 120 books, how many more books does he have to buy to make his library 90% full?"""
    # Define the capacity of the home library
    library_capacity = 400

    # Define the current number of books in the library
    current_books = 120

    # Calculate the number of books needed to make the library 90% full
    target_books = 0.9 * library_capacity
    additional_books = target_books - current_books

    # Display the number of additional books needed
    result = additional_books
    return result

print(solution())