def solution():
    """John buys cans of soup for buy 1 get one free. He gets 30 cans with a normal price of $0.60. How much does he pay?"""
    # Define the price per can of soup
    soup_price = 0.6

    # Calculate the number of cans John pays for (half of the total)
    paid_cans = 30 / 2

    # Calculate the total cost of the paid cans
    total_cost = paid_cans * soup_price

    # return the result
    result = total_cost
    return result

print(solution())