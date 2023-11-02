def solution():
    """Maggie has an after-school job that pays her $5.00 for every magazine subscription she can sell.  She sells 4 to her parents, 1 to her grandfather, 2 to the next-door neighbor and twice that amount to another neighbor.  How much money did Maggie earn?"""
    # Define the price per subscription
    PRICE_PER_SUBSCRIPTION = 5.00

    # Determine the number of subscriptions sold
    subscriptions_sold = 4 + 1 + 2 + (2 * 2)

    # Calculate Maggie's earnings
    earnings = subscriptions_sold * PRICE_PER_SUBSCRIPTION

    # Display Maggie's earnings
    result = earnings
    return result

print(solution())