def solution():
    """Tara is saving up to buy a new clarinet. She already has $10 saved. The clarinet costs $90. She plans to sell her old books to make the money. She sells each book of hers for $5. However, when she is halfway towards her goal, she loses all her savings and has to start over. How many books does she sell in total by the time she reaches her goal?"""
    # Define the cost of the clarinet and Tara's current savings
    CLARINET_COST = 90
    CURRENT_SAVINGS = 10

    # Define the cost of each book and the number of books sold
    BOOK_PRICE = 5
    books_sold = 0

    # Calculate the remaining amount needed to purchase the clarinet
    remaining_amount = CLARINET_COST - CURRENT_SAVINGS

    # While Tara has not yet reached her goal
    while remaining_amount > 0:
        # If she is halfway to her goal, she loses all her savings and starts over
        if CURRENT_SAVINGS >= CLARINET_COST / 2:
            CURRENT_SAVINGS = 0
            remaining_amount = CLARINET_COST

        # Determine how many books she needs to sell to reach her goal
        books_needed = (remaining_amount - CURRENT_SAVINGS) / BOOK_PRICE
        # Round up to the nearest whole number of books
        books_needed = int(books_needed) + (books_needed % 1 > 0)

        # Sell the necessary number of books and update her savings
        books_sold += books_needed
        CURRENT_SAVINGS += books_needed * BOOK_PRICE
        # Recalculate the remaining amount needed to purchase the clarinet
        remaining_amount = CLARINET_COST - CURRENT_SAVINGS

    # Return the total number of books sold
    result = books_sold
    return result

print(solution())