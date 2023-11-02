def solution():
    library_capacity = 400  # Karson's home library can hold 400 books
    current_books = 120  # Karson currently has 120 books
    percent_full = 0.9  # Karson wants his library to be 90% full

    # Calculate how many more books Karson needs to buy to make his library 90% full
    books_needed = round(library_capacity * percent_full) - current_books
    result = books_needed
    return result

print(solution())