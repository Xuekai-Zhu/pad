def solution():
    books_before = 56
    shelves = 4
    avg_books_per_shelf = 20
    leftover_books = 2

    # Calculate the total number of books that can fit in the bookcase
    total_books = shelves * avg_books_per_shelf

    # Calculate the number of books that Adam had filled before adding new books
    filled_books = total_books - leftover_books

    # Calculate the number of books Adam bought on his trip
    books_bought = filled_books - books_before

    result = books_bought
    return result

print(solution())