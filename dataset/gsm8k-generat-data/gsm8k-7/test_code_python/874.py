def solution():
    num_quarters = 14
    quarter_value = 25  # in cents

    # Calculate the total value of all quarters
    total_quarter_value = num_quarters * quarter_value

    # Calculate the value of half a dollar in cents
    candy_cost = 50  # in cents

    # Calculate the remaining value of Winston's quarters after buying candy
    remaining_value = total_quarter_value - candy_cost
    result = remaining_value
    return result

print(solution())