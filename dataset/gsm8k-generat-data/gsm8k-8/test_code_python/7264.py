def solution():
    # Define the capacity and current number of books
    capacity = 400
    current_books = 120

    # Calculate the number of books needed to fill 90% of the capacity
    target_books = 0.9 * capacity

    # Calculate the number of books left to buy
    books_to_buy = target_books - current_books
    result = books_to_buy
    return result

print(solution())