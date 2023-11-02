def solution():
    """Kendall is counting her change. She has a total of $4 in quarters, dimes, and nickels. If she has 10 quarters and 12 dimes, how many nickels does she have?"""
    # Define the value of each coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5

    # Define the number of each coin Kendall has
    num_quarters = 10
    num_dimes = 12

    # Calculate the total value of Kendall's change in cents
    total_value = (num_quarters * QUARTER_VALUE) + (num_dimes * DIME_VALUE)

    # Calculate the total number of nickels Kendall has
    num_nickels = (400 - total_value) / NICKEL_VALUE

    # Display the total number of nickels
    result = num_nickels
    return result

print(solution())