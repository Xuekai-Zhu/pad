def solution():
    total_books = 9900  # The library has 9,900 books
    remaining_fraction = 4/6  # Only four-sixths of the books are left
    remaining_books = total_books * remaining_fraction  # Calculate the number of remaining books

    # Calculate the number of books that were sold
    sold_books = total_books - remaining_books
    result = sold_books
    return result

print(solution())