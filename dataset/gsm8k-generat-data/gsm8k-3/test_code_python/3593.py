def solution():
    """Kate wants to buy a special pen as a gift for her friend. The pen costs $30, and Kate only has money for a third of that amount. How much more money does she need to buy the pen?"""
    # Define the cost of the pen and how much Kate has
    PEN_COST = 30
    KATE_HAS = PEN_COST / 3

    # Calculate how much more Kate needs to buy the pen
    MORE_NEEDED = PEN_COST - KATE_HAS

    # Display how much more Kate needs
    result = MORE_NEEDED
    return result

print(solution())