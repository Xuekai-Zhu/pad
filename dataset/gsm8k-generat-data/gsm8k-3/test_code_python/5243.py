def solution():
    """With her savings, Sara bought two books: a book for 5.5£ and a book for 6.5£. She gives a 20£ bill to the seller. How much change does she get back?"""
    # Define the cost of each book
    BOOK_1_PRICE = 5.5
    BOOK_2_PRICE = 6.5

    # Define the amount of money given to the seller
    AMOUNT_PAID = 20

    # Calculate the total cost of the books
    total_cost = BOOK_1_PRICE + BOOK_2_PRICE

    # Calculate the amount of change Sara should receive
    change = AMOUNT_PAID - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())