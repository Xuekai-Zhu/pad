def solution():
    """Charlotte needs to know how much money to have with her when she goes to the shoe store. How much money should Charlotte bring to buy a pair of boots, if the original price is $90 and there is a discount of 20%?"""
    # Define the original price and the discount percentage
    orig_price = 90
    discount_percent = 0.2

    # Calculate the discounted price
    discount_price = orig_price * (1 - discount_percent)

    # Return the discounted price
    result = discount_price
    return result

print(solution())