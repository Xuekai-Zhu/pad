def solution():
    """I bought a pair of shoes for $51. The shoes were already marked 75% off. What is the original price of the shoes?"""
    # Define the price of the shoes after 75% discount
    price_after_discount = 51

    # Calculate the original price of the shoes
    original_price = price_after_discount / (1 - 0.75)

    # Display the original price of the shoes
    result = original_price
    return result

print(solution())