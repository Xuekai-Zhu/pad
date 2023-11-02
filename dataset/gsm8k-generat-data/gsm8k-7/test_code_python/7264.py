def solution():
    library_capacity = 400
    current_books = 120
    percentage_full = 0.9   # 90% full

    # Calculate the number of books needed to fill the library to 90%
    books_needed = int(library_capacity * percentage_full) - current_books

    result = books_needed
    return result

print(solution())