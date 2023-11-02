def solution():
    num_quarters = 10
    num_dimes = 3
    num_nickels = 4
    num_pennies = 200

    # Calculate the total value of all the quarters
    total_quarters_value = num_quarters * 0.25

    # Calculate the total value of all the dimes
    total_dimes_value = num_dimes * 0.10

    # Calculate the total value of all the nickels
    total_nickels_value = num_nickels * 0.05

    # Calculate the total value of all the pennies
    total_pennies_value = num_pennies * 0.01

    # Calculate the total value of all the coins in dollars
    total_value_in_dollars = total_quarters_value + total_dimes_value + total_nickels_value + total_pennies_value

    result = total_value_in_dollars
    return result

print(solution())