def solution():
    """Todd bought a pair of jeans that cost $125 at full price. The jeans were on sale for 20% off. He then applied a coupon that took off $10. He paid with a store credit card that gave him another 10% off the remaining amount. How many dollars did he save on the original price of the jeans?"""
    # Define the initial price of the jeans
    initial_price = 125

    # Calculate the price of the jeans after the discount
    discounted_price = initial_price * 0.8 - 10

    # Calculate the final price after the credit card discount
    final_price = discounted_price * 0.9

    # Calculate the amount saved on the original price
    saved_amount = initial_price - final_price

    result = saved_amount
    return result

print(solution())