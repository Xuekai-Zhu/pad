def solution():
    total_change = 4.0  # in dollars
    num_quarters = 10
    num_dimes = 12

    # Calculate the total value of quarters and dimes
    value_quarters = num_quarters * 0.25
    value_dimes = num_dimes * 0.1

    # Calculate the remaining value of the change
    remaining_change = total_change - value_quarters - value_dimes

    # Calculate the number of nickels
    num_nickels = remaining_change / 0.05
    result = num_nickels
    return result

print(solution())