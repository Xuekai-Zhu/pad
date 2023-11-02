def solution():
    """Tara is saving up to buy a new clarinet. She already has $10 saved. The clarinet costs $90. She plans to sell her old books to make the money. She sells each book of hers for $5. However, when she is halfway towards her goal, she loses all her savings and has to start over. How many books does she sell in total by the time she reaches her goal?"""
    # Define the cost of the clarinet and the initial savings
    CLARINET_COST = 90
    INITIAL_SAVINGS = 10

    # Define the price per book and the number of books sold
    BOOK_PRICE = 5
    books_sold = 0

    # Initialize the total savings and the halfway point
    total_savings = INITIAL_SAVINGS
    halfway_point = (CLARINET_COST - INITIAL_SAVINGS) / 2

    # Sell books until the total savings is enough to buy the clarinet
    while total_savings < CLARINET_COST:
        # Sell a book and add the earnings to the total savings
        total_savings += BOOK_PRICE
        books_sold += 1

        # Check if the halfway point has been reached, and restart if necessary
        if total_savings >= halfway_point:
            total_savings = 0

    # return the result
    result = books_sold
    return result

print(solution())