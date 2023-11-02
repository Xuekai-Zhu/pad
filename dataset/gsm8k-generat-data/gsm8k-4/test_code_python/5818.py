def solution():
    """Tommy is looking at his change collection. He has 10 more dimes than pennies. He has twice as many nickels as dimes.
    He has 4 quarters. He has 10 times as many pennies as quarters. How many nickels does he have?"""
    # Define the value of each coin
    PENNY_VALUE = 0.01
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.1
    QUARTER_VALUE = 0.25

    # Define the number of quarters
    quarters = 4

    # Calculate the number of pennies
    pennies = quarters * 10

    # Calculate the number of dimes
    dimes = pennies + 10

    # Calculate the number of nickels
    nickels = dimes * 2

    # Calculate the total value of the coins
    total_value = pennies * PENNY_VALUE + nickels * NICKEL_VALUE + dimes * DIME_VALUE + quarters * QUARTER_VALUE

    result = nickels
    return result

print(solution())