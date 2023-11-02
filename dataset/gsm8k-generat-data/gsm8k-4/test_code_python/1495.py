def solution():
    """In a bookstore, a book costs $5. When Sheryll bought 10 books, she was given a discount of $0.5 each. How much did Sheryll pay in all?"""
    # Define the price of each book and the number purchased
    BOOK_PRICE = 5
    BOOKS_PURCHASED = 10

    # Define the discount per book and calculate the total cost
    DISCOUNT_PER_BOOK = 0.5
    total_cost = (BOOK_PRICE * BOOKS_PURCHASED) - (DISCOUNT_PER_BOOK * BOOKS_PURCHASED)

    # Return the result
    result = total_cost
    return result

print(solution())