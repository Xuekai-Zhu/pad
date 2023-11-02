def solution():
    # Define the original price of the jeans
    original_price = 125

    # Calculate the price after the first discount
    discount_price = original_price * 0.8

    # Calculate the price after the coupon
    coupon_price = discount_price - 10

    # Calculate the final price after the store credit card discount
    final_price = coupon_price * 0.9

    # Calculate the amount saved on the original price
    amount_saved = original_price - final_price
    result = amount_saved
    return result

print(solution())