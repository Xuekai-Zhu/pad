def solution():
    """The dog toys Samantha buys for her dog are "buy one get one half off" and all cost $12.00 each. She buys 4 toys. How much does she spend on dog toys?"""
    # Calculate the price of two dog toys with the "buy one get one half off" discount
    discounted_price = 12 * 1.5

    # Calculate the total price for four dog toys, with the discount applied to two of them
    total_price = (discounted_price * 2) + (12 * 2)

    # Return the total price
    result = total_price
    return result

print(solution())