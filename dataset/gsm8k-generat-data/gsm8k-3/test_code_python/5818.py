def solution():
    """Tommy is looking at his change collection. He has 10 more dimes than pennies. He has twice as many nickels as dimes. He has 4 quarters. He has 10 times as many pennies as quarters. How many nickels does he have?"""
    # Define the value of each type of coin in cents
    PENNY_VALUE = 1
    NICKEL_VALUE = 5
    DIME_VALUE = 10
    QUARTER_VALUE = 25

    # Define the number of each type of coin Tommy has
    pennies = x
    dimes = pennies + 10
    nickels = dimes * 2
    quarters = 4
    pennies = quarters * 10

    # Calculate the total value of Tommy's change
    total_value = (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)

    # Calculate the number of nickels Tommy has
    num_nickels = total_value // NICKEL_VALUE

    # Display the number of nickels Tommy has
    result = num_nickels
    return result

print(solution())