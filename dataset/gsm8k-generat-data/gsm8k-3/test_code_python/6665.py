def solution():
    """Tom finds 10 quarters, 3 dimes, and 4 nickels and 200 pennies. In dollars, how much money did he find?"""
    # Define the value of each coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Calculate the total value of the quarters
    quarter_total = 10 * QUARTER_VALUE

    # Calculate the total value of the dimes
    dime_total = 3 * DIME_VALUE

    # Calculate the total value of the nickels
    nickel_total = 4 * NICKEL_VALUE

    # Calculate the total value of the pennies
    penny_total = 200 * PENNY_VALUE

    # Calculate the total value in cents
    total_value = quarter_total + dime_total + nickel_total + penny_total

    # Convert the total value to dollars
    total_dollars = total_value / 100

    # Display the total value in dollars
    result = total_dollars
    return result

print(solution())