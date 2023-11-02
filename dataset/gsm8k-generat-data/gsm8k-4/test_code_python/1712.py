def solution():
    """Marlene wants to buy half a dozen of shirts to avail of the sale. The regular price of a shirt is $50 and is now on sale at a 20% discount. How much will Marlene pay for the shirts?"""
    # Define the regular price of a shirt
    shirt_price = 50

    # Calculate the discounted price of a shirt
    discounted_price = shirt_price * 0.8

    # Calculate the price of half a dozen shirts
    total_price = discounted_price * 6

    result = total_price
    return result

print(solution())