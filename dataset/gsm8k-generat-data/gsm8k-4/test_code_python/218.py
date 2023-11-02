def solution():
    """Ravi has some coins. He has 2 more quarters than nickels and 4 more dimes than quarters. If he has 6 nickels, how much money does he have?"""
    # Define the value of each coin
    NICKEL_VALUE = 0.05
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.10

    # Define the number of nickels
    nickels = 6

    # Calculate the number of quarters and dimes
    quarters = nickels + 2
    dimes = quarters + 4

    # Calculate the total value of the coins
    total_value = (nickels * NICKEL_VALUE) + (quarters * QUARTER_VALUE) + (dimes * DIME_VALUE)

    # Return the total value
    result = round(total_value, 2)
    return result

print(solution())