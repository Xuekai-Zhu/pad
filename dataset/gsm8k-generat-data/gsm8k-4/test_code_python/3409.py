def solution():
    """Peter needs 80 ounces of soda for his party. He sees that 8 oz cans cost $.5 each. How much does he spend on soda if he buys the exact number of cans he needs?"""
    # Define the necessary amount of soda
    necessary_soda = 80

    # Define the size of a can of soda
    can_size = 8

    # Define the price of a can of soda
    can_price = 0.5

    # Calculate the number of cans needed
    cans_needed = necessary_soda / can_size

    # Calculate the total cost of the soda
    total_cost = cans_needed * can_price

    result = total_cost
    return result

print(solution())