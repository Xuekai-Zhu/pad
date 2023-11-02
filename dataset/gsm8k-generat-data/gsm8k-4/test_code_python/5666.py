def solution():
    """Steve is holding nickels and dimes in his hand. He has 4 more dimes than nickels. He has a total of 70 cents in his hand. How many nickels is he holding?"""
    # Define the value of a nickel and a dime
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.10

    # Define the number of nickels and dimes
    nickels = None
    dimes = None

    # Set up the equations for the number of coins and their total value
    # Let x be the number of nickels, then the number of dimes is x + 4
    # The total value of the nickels is 0.05x, and the total value of the dimes is 0.10(x + 4)
    # The total value of the coins is 0.05x + 0.10(x + 4) = 0.15x + 0.40
    # We also know that the total value of the coins is 0.70
    # So we can set up the equation 0.15x + 0.40 = 0.70 and solve for x

    x = (0.70 - 0.40) / 0.15
    nickels = round(x)

    result = nickels
    return result

print(solution())