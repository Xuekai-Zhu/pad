def solution():
    # Number of books she shelved from the top section of the cart
    top_books = 12 + 8 + 4

    # Number of mystery books on the bottom section of the cart
    bottom_mystery_books = top_books / 2

    # Number of remaining books on the bottom section of the cart
    remaining_bottom_books = 5 + 6 + bottom_mystery_books

    # Total number of books on the cart when she started
    total_books = top_books + remaining_bottom_books
    result = total_books
    return result

print(solution())