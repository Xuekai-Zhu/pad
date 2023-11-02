def solution():
    top_history_books = 12
    top_romance_books = 8
    top_poetry_books = 4
    bottom_mystery_books = 0.5 * (top_history_books + top_romance_books + top_poetry_books)
    bottom_western_books = 5
    bottom_biography_books = 6

    # Calculate the total number of books on the top section of the cart
    top_total_books = top_history_books + top_romance_books + top_poetry_books

    # Calculate the total number of books on the bottom section of the cart
    bottom_total_books = bottom_mystery_books + bottom_western_books + bottom_biography_books

    # Calculate the total number of books on the cart
    total_books_on_cart = top_total_books + bottom_total_books
    result = total_books_on_cart
    return result

print(solution())