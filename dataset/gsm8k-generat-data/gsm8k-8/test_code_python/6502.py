def solution():
    # Define the value of a penny and a dime in dollars
    penny_value = 0.01
    dime_value = 0.1

    # Calculate the value of the pennies and dimes in each piggy bank
    piggy_bank1_value = 100 * penny_value + 50 * dime_value
    piggy_bank2_value = 100 * penny_value + 50 * dime_value

    # Calculate the total value of Ivan's savings
    total_value = piggy_bank1_value + piggy_bank2_value

    # Round the total value to two decimal points
    result = round(total_value, 2)
    return result

print(solution())