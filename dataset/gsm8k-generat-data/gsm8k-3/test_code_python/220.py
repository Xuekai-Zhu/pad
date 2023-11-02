def solution():
    """Ravi has some coins. He has 2 more quarters than nickels and 4 more dimes than quarters. If he has 6 nickels, how much money does he have?"""
    # Define the value of each coin in cents
    NICKEL_VALUE = 5
    DIME_VALUE = 10
    QUARTER_VALUE = 25

    # Define the number of nickels Ravi has
    num_nickels = 6

    # Calculate the number of quarters Ravi has
    num_quarters = num_nickels + 2

    # Calculate the number of dimes Ravi has
    num_dimes = num_quarters + 4

    # Calculate the total value of Ravi's coins in cents
    total_value = (num_nickels * NICKEL_VALUE) + (num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE)

    # Convert the total value to dollars and cents
    dollars = total_value // 100
    cents = total_value % 100

    # Display Ravi's total money
    result = f"${dollars}.{cents:02}"
    return result

print(solution())