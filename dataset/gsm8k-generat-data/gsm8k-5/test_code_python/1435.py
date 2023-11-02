def solution():
    # Convert the number of each coin to its value in dollars
    quarters_value = 0.25 * 10
    dimes_value = 0.10 * 3
    nickels_value = 0.05 * 3
    pennies_value = 0.01 * 5

    # Calculate the total value of the coins found
    total_value = quarters_value + dimes_value + nickels_value + pennies_value
    result = total_value
    return result

print(solution())