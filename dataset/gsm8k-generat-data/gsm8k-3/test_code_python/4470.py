def solution():
    """Tim buys a cabinet for $1200 and gets a 15% discount.  How much did he pay?"""
    # Define the original price and discount percentage
    ORIGINAL_PRICE = 1200
    DISCOUNT_PERCENTAGE = 0.15

    # Calculate the discount amount
    discount_amount = ORIGINAL_PRICE * DISCOUNT_PERCENTAGE

    # Calculate the final price after discount
    final_price = ORIGINAL_PRICE - discount_amount

    # Display the final price
    result = final_price
    return result

print(solution())