def solution():
    """Marlene wants to buy half a dozen of shirts to avail of the sale.
    The regular price of a shirt is $50 and is now on sale at a 20% discount.
    How much will Marlene pay for the shirts?"""
    
    # Define the regular price and discount percentage
    REGULAR_PRICE = 50
    DISCOUNT_PERCENTAGE = 20

    # Calculate the discounted price
    discounted_price = REGULAR_PRICE - (REGULAR_PRICE * DISCOUNT_PERCENTAGE / 100)

    # Calculate the total cost of half a dozen shirts
    total_cost = discounted_price * 6 / 2 

    # Display the total cost
    result = total_cost
    return result

print(solution())