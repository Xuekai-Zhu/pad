def solution():
    """Alice has 20 quarters. She wants to exchange them for nickels and so she goes to the bank. After getting back from the bank, she discovers that 20% of the nickels are iron nickels worth $3 each. What is the total value of her money now?"""
    # Define the value of a quarter and a nickel
    QUARTER_VALUE = 0.25
    NICKEL_VALUE = 0.05

    # Calculate the total value of the quarters
    total_quarters_value = 20 * QUARTER_VALUE

    # Calculate the number of nickels received from the bank
    nickels_received = total_quarters_value / NICKEL_VALUE

    # Calculate the number of iron nickels received
    iron_nickels = nickels_received * 0.2

    # Calculate the total value of the iron nickels
    iron_nickels_value = iron_nickels * 3

    # Calculate the total value of the money now
    total_value = total_quarters_value + (nickels_received - iron_nickels) * NICKEL_VALUE + iron_nickels_value

    result = total_value
    return result

print(solution())