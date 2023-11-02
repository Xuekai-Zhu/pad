def solution():
    # Calculate the number of books Karson needs to buy to fill his library 90%
    capacity = 400
    current_books = 120
    target_books = 0.9 * capacity
    books_to_buy = target_books - current_books
    result = books_to_buy
    return result

print(solution())