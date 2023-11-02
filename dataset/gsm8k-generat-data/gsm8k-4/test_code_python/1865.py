def solution():
    """Linda's bag has 2 dimes, 6 quarters, and 5 nickels. Her mother gives her 2 more dimes, 10 quarters, and twice as many nickels as she has. How many coins does she have altogether?"""
    # Define the initial number of coins
    dimes = 2
    quarters = 6
    nickels = 5

    # Add the coins given by Linda's mother
    dimes += 2
    quarters += 10
    nickels *= 2

    # Calculate the total number of coins
    total_coins = dimes + quarters + nickels

    # return the result
    result = total_coins
    return result

print(solution())