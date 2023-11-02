def solution():
    # Define the number of pennies and calculate the number of nickels, dimes, and quarters
    num_pennies = 120
    num_nickels = num_pennies // 3
    num_dimes = num_nickels // 5
    num_quarters = num_dimes * 2

    # Calculate the total value of each type of coin
    penny_value = num_pennies * 0.01
    nickel_value = num_nickels * 0.05
    dime_value = num_dimes * 0.1
    quarter_value = num_quarters * 0.25

    # Calculate the total value of all the coins
    total_value = penny_value + nickel_value + dime_value + quarter_value
    result = total_value
    return result

print(solution())