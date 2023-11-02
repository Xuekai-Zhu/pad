def solution():
    """Kate wants to buy a special pen as a gift for her friend. The pen costs $30, and Kate only has money for a third of that amount. How much more money does she need to buy the pen?"""
    # Define the cost of the pen and the amount of money Kate has
    PEN_PRICE = 30
    KATE_MONEY = PEN_PRICE / 3

    # Calculate the amount of money Kate still needs to buy the pen
    still_needs = PEN_PRICE - KATE_MONEY

    # Return the result
    result = still_needs
    return result

print(solution())