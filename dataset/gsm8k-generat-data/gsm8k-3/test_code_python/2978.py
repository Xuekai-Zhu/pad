def solution():
    """James buys 3 shirts for $60.  There is a 40% off sale.  How much did he pay per shirt after the discount?"""
    # Define the original price per shirt and the discount percentage
    ORIGINAL_PRICE = 20
    DISCOUNT_PERCENTAGE = 40

    # Calculate the total cost before the discount
    original_cost = ORIGINAL_PRICE * 3

    # Calculate the amount of the discount
    discount_amount = original_cost * (DISCOUNT_PERCENTAGE / 100)

    # Calculate the total cost after the discount
    discounted_cost = original_cost - discount_amount

    # Calculate the price per shirt after the discount
    price_per_shirt = discounted_cost / 3

    # Display the price per shirt after the discount
    result = price_per_shirt
    return result

print(solution())