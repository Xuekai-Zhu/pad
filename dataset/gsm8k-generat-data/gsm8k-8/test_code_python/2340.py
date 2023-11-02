def solution():
    # Calculate the total number of books Jamal shelve
    total_shelved_books = 12 + 19 + 8 + 4

    # Calculate the total number of books to shelve
    total_books = total_shelved_books + 16

    # Calculate the number of books Jamal started with in the cart
    start_cart_books = total_books - total_shelved_books
    result = start_cart_books
    return result

print(solution())