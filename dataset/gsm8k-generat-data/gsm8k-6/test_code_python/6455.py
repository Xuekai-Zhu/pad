def solution():
    # Calculate the total number of books in the bookcase before adding new books
    initial_books = 56

    # Calculate the total number of books that can fit in the bookcase
    total_capacity = 4 * 20

    # Calculate the number of extra books after completely filling the bookcase
    extra_books = 2

    # Calculate the number of books Adam bought on his shopping trip
    books_bought = total_capacity - initial_books - extra_books

    result = books_bought
    return result

print(solution())