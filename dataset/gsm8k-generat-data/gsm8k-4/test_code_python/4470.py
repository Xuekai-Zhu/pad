def solution():
    """Tim buys a cabinet for $1200 and gets a 15% discount. How much did he pay?"""
    # Define the original price and the discount percentage
    original_price = 1200
    discount_percentage = 0.15

    # Calculate the discount amount and the final price
    discount_amount = original_price * discount_percentage
    final_price = original_price - discount_amount

    # Return the final price
    result = final_price
    return result

print(solution())