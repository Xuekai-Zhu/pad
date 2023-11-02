def solution():
    """You can lower the price by 20% if you buy more than fifteen units of iPhone cases. If you pay $500 to buy 18 units, what is the original price?"""
    # Define the price per iPhone case
    price = None

    # Define the number of iPhone cases bought
    quantity = 18

    if quantity > 15:
        # Apply the 20% discount
        discounted_price = 0.8 * 500
        
        # Calculate the original price
        price = discounted_price / quantity * 20
    else:
        price = 500 / quantity

    result = price
    return result

print(solution())