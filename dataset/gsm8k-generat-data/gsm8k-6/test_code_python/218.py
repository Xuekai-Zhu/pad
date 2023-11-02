def solution():
    # Calculate the number of quarters Ravi has
    num_nickels = 6  # given that Ravi has 6 nickels
    num_quarters = num_nickels + 2  # Ravi has 2 more quarters than nickels
    num_dimes = num_quarters + 4  # Ravi has 4 more dimes than quarters

    # Calculate the total value of the coins Ravi has in dollars
    total_value = (0.05 * num_nickels) + (0.10 * num_dimes) + (0.25 * num_quarters)
    result = total_value
    return result

print(solution())