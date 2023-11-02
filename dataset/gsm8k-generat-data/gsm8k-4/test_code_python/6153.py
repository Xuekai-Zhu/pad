def solution():
    """To buy a book, you pay $20 for each of the first 5 books at the supermarket, and for each additional book you buy over $20, you receive a discount of $2. If Beatrice bought 20 books, how much did she pay at the supermarket?"""
    # Define the base price for the first 5 books and the discount amount for additional books
    BASE_PRICE = 20
    DISCOUNT_AMOUNT = 2

    # Define the number of books Beatrice bought
    num_books = 20

    # Calculate the total cost of the first 5 books
    total_cost = BASE_PRICE * 5

    # Calculate the total cost of the remaining books with the discount
    for i in range(6, num_books + 1):
        total_cost += (BASE_PRICE - DISCOUNT_AMOUNT)

    result = total_cost
    return result

print(solution())