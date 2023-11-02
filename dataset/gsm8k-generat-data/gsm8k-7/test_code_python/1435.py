def solution():
    num_quarters = 10
    num_dimes = 3
    num_nickels = 3
    num_pennies = 5

    # Calculate the total value of the quarters
    quarters_value = num_quarters * 0.25

    # Calculate the total value of the dimes
    dimes_value = num_dimes * 0.1

    # Calculate the total value of the nickels
    nickels_value = num_nickels * 0.05

    # Calculate the total value of the pennies
    pennies_value = num_pennies * 0.01

    # Calculate the total value of all the coins Harriett found
    total_value = quarters_value + dimes_value + nickels_value + pennies_value
    result = total_value
    return result

print(solution())