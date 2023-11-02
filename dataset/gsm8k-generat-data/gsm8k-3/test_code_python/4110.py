def solution():
    """Michael buys his suit for $430 and shoes for $190. So, if he gets a $100 discount, what was the amount that he paid to the seller?"""
    # Define the original prices
    SUIT_PRICE = 430
    SHOES_PRICE = 190

    # Calculate the total cost before discount
    total_cost = SUIT_PRICE + SHOES_PRICE

    # Apply the discount
    total_cost -= 100

    # Display the amount paid to the seller
    result = total_cost
    return result

print(solution())