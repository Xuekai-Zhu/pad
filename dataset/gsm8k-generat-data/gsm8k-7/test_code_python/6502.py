def solution():
    pennies = 100
    dimes = 50
    penny_value = 0.01
    dime_value = 0.1

    # Calculate the total value of all pennies
    total_pennies_value = pennies * penny_value

    # Calculate the total value of all dimes
    total_dimes_value = dimes * dime_value

    # Calculate the total value of both piggy banks
    total_value = total_pennies_value + total_dimes_value
    result = total_value
    return result

print(solution())