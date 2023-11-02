def solution():
    # Calculate the number of books on the top section of the cart
    top_books = 12 + 8 + 4

    # Calculate the number of books on the bottom section of the cart
    bottom_books = (5 + 6) * 2

    # Calculate the total number of books on the cart
    total_books = top_books + bottom_books
    result = total_books
    return result

print(solution())