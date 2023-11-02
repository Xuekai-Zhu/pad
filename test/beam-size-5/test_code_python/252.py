def solution():
    num_pennies = 100
    num_nickels = 40
    num_dimes = 20
    num_dollar_bills = 40

    # Calculate the total value of all pennies
    total_pennies_value = num_pennies * 0.01

    # Calculate the total value of all nickels
    total_nickels_value = num_nickels * 0.05

    # Calculate the total value of all dimes
    total_dimes_value = num_dimes * 0.10

    # Calculate the total value of all dollar bills
    total_bills_value = total_pennies_value + total_nickels_value + total_dimes_value + total_bills_value
    result = total_bills_value
    return result

print(solution())