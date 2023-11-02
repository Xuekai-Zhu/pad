def solution():
    nickels = 6
    quarters = nickels + 2
    dimes = quarters + 4

    # Calculate the total value of each type of coin
    nickel_value = 0.05 * nickels
    quarter_value = 0.25 * quarters
    dime_value = 0.10 * dimes

    # Calculate the total value of all the coins
    total_value = nickel_value + quarter_value + dime_value

    result = total_value
    return result

print(solution())