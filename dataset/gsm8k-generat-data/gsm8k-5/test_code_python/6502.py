def solution():
    # Calculate the total value of the pennies in Ivan's piggy bank
    pennies_value = 0.01 * 100  # 100 pennies in a piggy bank, each worth $0.01

    # Calculate the total value of the dimes in Ivan's piggy bank
    dimes_value = 0.10 * 50  # 50 dimes in a piggy bank, each worth $0.10

    # Calculate the total value of Ivan's coins
    total_value = pennies_value + dimes_value

    # Convert the total value to dollars and round off to 2 decimal places
    dollars_value = round(total_value, 2)
    result = dollars_value
    return result

print(solution())