def solution():
    # Value of each type of coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    # Number of piles for each type of coin
    num_quarter_piles = 4
    num_dime_piles = 6
    num_nickel_piles = 9
    num_penny_piles = 5

    # Calculate the total value of each type of coin
    total_quarters = num_quarter_piles * 10 * quarter_value
    total_dimes = num_dime_piles * 10 * dime_value
    total_nickels = num_nickel_piles * 10 * nickel_value
    total_pennies = num_penny_piles * 10 * penny_value

    # Calculate the total value of all coins
    total_value = total_quarters + total_dimes + total_nickels + total_pennies
    result = total_value
    return result

print(solution())