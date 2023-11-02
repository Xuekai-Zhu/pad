def solution():
    # Define the value of each coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the total value of the coins found
    total_value = 10 * quarter_value + 3 * dime_value + 3 * nickel_value + 5 * penny_value

    result = total_value
    return result

print(solution())