def solution():
    """Tom finds 10 quarters, 3 dimes, and 4 nickels and 200 pennies. In dollars, how much money did he find?"""
    # Define the value of each type of coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the total value of the quarters
    quarter_total = 10 * quarter_value

    # Calculate the total value of the dimes
    dime_total = 3 * dime_value

    # Calculate the total value of the nickels
    nickel_total = 4 * nickel_value

    # Calculate the total value of the pennies
    penny_total = 200 * penny_value

    # Calculate the total value of all the coins
    total_value = quarter_total + dime_total + nickel_total + penny_total

    # Return the result in dollars
    result = total_value
    return result

print(solution())