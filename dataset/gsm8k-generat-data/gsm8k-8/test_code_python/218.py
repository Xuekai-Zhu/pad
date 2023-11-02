def solution():
    # Number of nickels Ravi has
    num_nickels = 6

    # Calculate the number of quarters Ravi has
    num_quarters = num_nickels + 2

    # Calculate the number of dimes Ravi has
    num_dimes = num_quarters + 4

    # Calculate the total value of Ravi's coins
    total_value = num_nickels * 0.05 + num_quarters * 0.25 + num_dimes * 0.1

    result = total_value
    return result

print(solution())