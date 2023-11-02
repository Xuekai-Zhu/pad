def solution():
    num_nickels = 20
    num_dimes = 3 * num_nickels
    new_nickels = 2 * num_nickels

    # Calculate the total value of the old nickels
    old_nickels_value = num_nickels * 0.05

    # Calculate the total value of the new nickels
    new_nickels_value = new_nickels * 0.05

    # Calculate the total value of the dimes
    dimes_value = num_dimes * 0.10

    # Calculate the total value of all the coins
    total_value = old_nickels_value + new_nickels_value + dimes_value
    result = total_value
    return result

print(solution())