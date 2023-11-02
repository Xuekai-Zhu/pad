def solution():
    num_dimes = 4
    num_quarters = 4  # originally
    num_nickels = 7
    num_additional_quarters = 5

    # Calculate the total value of the original quarters, dimes, and nickels
    total_value_original_coins = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickels * 0.05)

    # Calculate the value of the additional quarters given by Maria's mom
    additional_quarters_value = num_additional_quarters * 0.25

    # Calculate the new total value of all coins
    new_total_value = total_value_original_coins + additional_quarters_value

    result = new_total_value
    return result

print(solution())