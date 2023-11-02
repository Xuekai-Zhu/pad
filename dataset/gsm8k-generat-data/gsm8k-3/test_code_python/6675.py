def solution():
    """James buys 6 t-shirts for 50% off.  They each cost $20.  How much did he pay?"""
    # Define the original price of one t-shirt
    ORIGINAL_PRICE = 20

    # Calculate the discounted price of one t-shirt
    DISCOUNTED_PRICE = ORIGINAL_PRICE * 0.5

    # Calculate the cost of 6 t-shirts at the discounted price
    total_cost = DISCOUNTED_PRICE * 6

    # Display the total cost
    result = total_cost
    return result

print(solution())