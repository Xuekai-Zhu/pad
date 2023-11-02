def solution():
    """Kendall is counting her change. She has a total of $4 in quarters, dimes, and nickels. If she has 10 quarters and 12 dimes, how many nickels does she have?"""
    # Define the values of a quarter, dime, and nickel in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5

    # Define the total amount of change in cents
    total_change = 400

    # Calculate the total value of quarters and dimes
    quarters_value = 10 * QUARTER_VALUE
    dimes_value = 12 * DIME_VALUE
    total_quarters_dimes_value = quarters_value + dimes_value

    # Calculate the total value of nickels by subtracting the value of quarters and dimes from the total change
    nickels_value = total_change - total_quarters_dimes_value

    # Calculate the number of nickels
    nickels = nickels_value // NICKEL_VALUE

    # return the result
    result = nickels
    return result

print(solution())