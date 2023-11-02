def solution():
    """Ivan has a piggy bank that can hold 100 pennies and 50 dimes. How much, in dollars, does Ivan have if he has filled his two piggy banks with those coins?"""
    # Define the value of each coin in cents
    PENNY_VALUE = 1
    DIME_VALUE = 10

    # Define the capacity of each piggy bank
    PENNY_CAPACITY = 100
    DIME_CAPACITY = 50

    # Calculate the total value of pennies
    total_pennies = PENNY_VALUE * PENNY_CAPACITY * 2

    # Calculate the total value of dimes
    total_dimes = DIME_VALUE * DIME_CAPACITY * 2

    # Calculate the total value in dollars
    total_value = (total_pennies + total_dimes) / 100

    # Display the total value in dollars
    result = total_value
    return result

print(solution())