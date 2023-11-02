def solution():
    # Calculate the number of dimes Val has
    num_dimes = 3 * 20 / 10  # Val has three times as many dimes as nickels, and she had 20 nickels before finding the new ones

    # Calculate the number of nickels Val has after finding the new ones
    num_nickels = 2 * 20  # Val accidentally finds twice as many nickels as she has, which is 20, in her brother's treasure box

    # Calculate the total value of money Val has
    total_value = 0.05 * (20 + num_nickels) + 0.10 * num_dimes  # the value of each nickel is $0.05, the value of each dime is $0.10

    # Convert the total value to dollars
    value_in_dollars = total_value / 100

    result = value_in_dollars
    return result

print(solution())