def solution():
    # Define the value of each coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the total value of each type of coin
    quarter_total = 10 * 4 * quarter_value
    dime_total = 10 * 6 * dime_value
    nickel_total = 10 * 9 * nickel_value
    penny_total = 10 * 5 * penny_value

    # Calculate the total value of all the coins
    total_value = quarter_total + dime_total + nickel_total + penny_total
    result = total_value
    return result

print(solution())