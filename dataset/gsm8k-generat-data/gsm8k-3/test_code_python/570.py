def solution():
    """Cindy tosses 5 dimes into the wishing pond.  Eric flips 3 quarters into the pond.  Garrick throws in 8 nickels.  Ivy then drops 60 pennies in.  If Eric dips his hands into the water and pulls out a quarter, how much money, in cents, did they put into the pond?"""
    # Define the value of each type of coin in cents
    DIME_VALUE = 10
    QUARTER_VALUE = 25
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Define the number of each type of coin thrown in
    num_dimes = 5
    num_quarters = 3
    num_nickels = 8
    num_pennies = 60

    # Calculate the total value of all the coins thrown in
    total_value = (num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE) + (num_nickels * NICKEL_VALUE) + (num_pennies * PENNY_VALUE)

    # Subtract the value of the quarter Eric took out
    total_value -= QUARTER_VALUE

    # Display the total value of the coins in cents
    result = total_value
    return result

print(solution())