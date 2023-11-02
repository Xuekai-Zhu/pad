def solution():
    """To buy a book, you pay $20 for each of the first 5 books at the supermarket, and for each additional book you buy over $20, you receive a discount of $2. If Beatrice bought 20 books, how much did she pay at the supermarket?"""
    # Define the cost of the first 5 books
    FIRST_FIVE_BOOKS_COST = 20

    # Define the discount per book after the first 5
    DISCOUNT_PER_BOOK = 2

    # Define the number of books Beatrice bought
    NUM_BOOKS = 20

    # Calculate the cost of the first 5 books
    first_five_cost = FIRST_FIVE_BOOKS_COST * 5

    # Calculate the cost of the remaining books with discount
    remaining_books_cost = 0
    for i in range(6, NUM_BOOKS + 1):
        remaining_books_cost += 20 - DISCOUNT_PER_BOOK * (i - 6)

    # Calculate the total cost
    total_cost = first_five_cost + remaining_books_cost

    result = total_cost
    return result

print(solution())