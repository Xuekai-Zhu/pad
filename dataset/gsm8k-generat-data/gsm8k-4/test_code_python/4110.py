def solution():
    """Michael buys his suit for $430 and shoes for $190. So, if he gets a $100 discount, what was the amount that he paid to the seller?"""
    # Define the prices of the suit and shoes
    suit_price = 430
    shoes_price = 190

    # Define the discount amount
    discount = 100

    # Calculate the total cost before discount
    total_cost = suit_price + shoes_price

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    # Return the result
    result = total_cost_after_discount
    return result

print(solution())