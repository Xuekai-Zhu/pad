def solution():
    """Leonard and his brother Michael bought presents for their father. Leonard bought a wallet at $50 and two pairs of sneakers at $100 each pair, while Michael bought a backpack at $100 and two pairs of jeans at $50 each pair. How much did they spend in all?"""
    # Define the prices of each item
    WALLET_PRICE = 50
    SNEAKERS_PRICE = 100
    BACKPACK_PRICE = 100
    JEANS_PRICE = 50

    # Calculate the total amount spent by Leonard
    leonard_total = WALLET_PRICE + (2 * SNEAKERS_PRICE)

    # Calculate the total amount spent by Michael
    michael_total = BACKPACK_PRICE + (2 * JEANS_PRICE)

    # Calculate the total amount spent by both brothers
    total_spent = leonard_total + michael_total

    # Display the total amount spent
    result = total_spent
    return result

print(solution())