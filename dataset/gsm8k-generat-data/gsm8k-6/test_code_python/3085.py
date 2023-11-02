def solution():
    # Calculate the number of coins in each jar
    num_pennies = 120  # given
    num_nickels = num_pennies * 3  # three times as many pennies as nickels
    num_dimes = num_nickels // 5  # five times as many nickels as dimes
    num_quarters = num_dimes * 2  # twice as many quarters as dimes

    # Calculate the total value of the coins
    total_value = num_pennies * 0.01 + num_nickels * 0.05 + num_dimes * 0.1 + num_quarters * 0.25
    result = total_value
    return result

print(solution())