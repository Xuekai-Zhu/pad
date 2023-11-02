def solution():
    """You can lower the price by 20% if you buy more than fifteen units of iPhone cases. If you pay $500 to buy 18 units, what is the original price?"""
    # Define the number of units purchased and the discounted price
    units = 18
    discounted_price = 500

    # Check if the number of units purchased is greater than 15
    if units > 15:
        # Calculate the original price based on the discounted price and discount percentage
        discount_percentage = 0.2
        original_price = discounted_price / (1 - discount_percentage)
    else:
        # If the number of units purchased is not greater than 15, assume the original price is the same as the discounted price
        original_price = discounted_price

    # Display the original price
    result = original_price
    return result

print(solution())