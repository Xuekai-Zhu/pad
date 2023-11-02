def solution():
    """James buys 3 shirts for $60. There is a 40% off sale. How much did he pay per shirt after the discount?"""
    # Define the original price of a shirt
    original_price = 20

    # Calculate the discounted price per shirt
    discounted_price = original_price * 0.6

    # Calculate the amount James paid for all 3 shirts
    total_cost = discounted_price * 3

    # Calculate the cost per shirt after the discount
    cost_per_shirt = total_cost / 3

    result = cost_per_shirt
    return result

print(solution())