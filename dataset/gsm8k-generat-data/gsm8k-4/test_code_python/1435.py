def solution():
    """When Harriett vacuumed the sofa and chair she found 10 quarters, 3 dimes, 3 nickels, and 5 pennies. How much money did Harriett find?"""
    
    # Define the value of each coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Calculate the value of the quarters
    quarters_value = 10 * QUARTER_VALUE

    # Calculate the value of the dimes
    dimes_value = 3 * DIME_VALUE

    # Calculate the value of the nickels
    nickels_value = 3 * NICKEL_VALUE

    # Calculate the value of the pennies
    pennies_value = 5 * PENNY_VALUE

    # Calculate the total value
    total_value = quarters_value + dimes_value + nickels_value + pennies_value

    # Convert the total value to dollars
    total_dollars = float(total_value) / 100

    # Return the result
    result = total_dollars
    return result

print(solution())