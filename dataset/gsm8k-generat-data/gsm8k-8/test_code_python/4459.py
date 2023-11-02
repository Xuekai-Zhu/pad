def solution():
    # Define the values of the coins
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05

    # Calculate the value of the quarters and dimes
    quarter_total_value = 10 * quarter_value
    dime_total_value = 12 * dime_value

    # Calculate the remaining value needed to reach $4
    remaining_value = 4 - quarter_total_value - dime_total_value

    # Calculate the number of nickels needed to reach the remaining value
    nickel_count = int(remaining_value / nickel_value)

    result = nickel_count
    return result

print(solution())