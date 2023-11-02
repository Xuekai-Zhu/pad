def solution():
    # Calculate the total number of pennies, dimes and nickels
    num_quarters = 4
    num_pennies = 10 * num_quarters
    num_dimes = num_pennies + 10
    num_nickels = 2 * num_dimes

    result = num_nickels
    return result

print(solution())