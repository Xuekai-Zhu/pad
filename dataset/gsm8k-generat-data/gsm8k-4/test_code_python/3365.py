def solution():
    """John buys 3 dress shirts. They sell for $20 each. He also has to pay 10% tax on everything. How much did he pay in total?"""
    # Define the number of dress shirts and the price per shirt
    NUM_SHIRTS = 3
    SHIRT_PRICE = 20

    # Calculate the total cost before tax
    total_cost_before_tax = NUM_SHIRTS * SHIRT_PRICE

    # Calculate the tax
    tax = 0.1 * total_cost_before_tax

    # Calculate the total cost including tax
    total_cost = total_cost_before_tax + tax

    # Return the result
    result = total_cost
    return result

print(solution())