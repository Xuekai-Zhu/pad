def solution():
    num_nickels = 6
    num_quarters = num_nickels + 2
    num_dimes = num_quarters + 4

    # Calculate the total value of all coins
    total_value = num_nickels * 0.05 + num_quarters * 0.25 + num_dimes * 0.1
    result = total_value
    return result

print(solution())