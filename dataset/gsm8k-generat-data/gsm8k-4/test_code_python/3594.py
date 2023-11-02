def solution():
    """Solomon bought a dining table at a 10% discount and paid the sale price of $450. What was the original price of the dining table?"""
    # Define the sale price and discount percentage
    sale_price = 450
    discount_percentage = 10

    # Calculate the original price of the dining table
    original_price = sale_price / (1 - (discount_percentage / 100))

    # Round the original price to the nearest dollar
    rounded_price = round(original_price)

    result = rounded_price
    return result

print(solution())