def solution():
    """Ivan has a piggy bank that can hold 100 pennies and 50 dimes. How much, in dollars, does Ivan have if he has filled his two piggy banks with those coins?"""
    # Define the value of one penny and one dime in dollars
    PENNY_VALUE = 0.01
    DIME_VALUE = 0.1

    # Calculate the total value of pennies
    total_pennies = 100 * 2
    pennies_value = total_pennies * PENNY_VALUE

    # Calculate the total value of dimes
    total_dimes = 50 * 2
    dimes_value = total_dimes * DIME_VALUE

    # Calculate the total value of Ivan's piggy banks
    total_value = pennies_value + dimes_value

    # Return the result in dollars
    result = total_value
    return result

print(solution())