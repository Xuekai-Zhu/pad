def solution():
    """A dime has the same value as 10 pennies and a nickel has the same value as 5 pennies.
    How many pennies will Grace have by exchanging her 10 dimes and 10 nickels?"""
    # Define the value of each coin
    dime_value = 10 * 1
    nickel_value = 5 * 1

    # Calculate the total value of the dimes and nickels in pennies
    total_value = (dime_value * 10) + (nickel_value * 10)

    # Display the total value in pennies
    result = total_value
    return result

print(solution())