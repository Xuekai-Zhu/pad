def solution():
    """Wally buys bears at the park. A bear is priced at $4.00 for the first bear and a discount of 50 cents per bear is given after that. How much does Wally pay for 101 bears?"""
    # Define the price of the first bear and the discount per bear
    FIRST_BEAR_PRICE = 4.00
    DISCOUNT_PER_BEAR = 0.50

    # Calculate the total price of the bears
    if (101 <= 1):
        total_price = FIRST_BEAR_PRICE
    else:
        total_price = FIRST_BEAR_PRICE + DISCOUNT_PER_BEAR * (101 - 1)

    # Display the total price
    result = total_price
    return result

print(solution())