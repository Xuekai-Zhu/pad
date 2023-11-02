def solution():
    # Calculate the total value of Rocco's coins
    total_quarters = 4 * 10 * 0.25  # 4 piles of quarters, 10 coins per pile, each quarter is worth 0.25
    total_dimes = 6 * 10 * 0.10  # 6 piles of dimes, 10 coins per pile, each dime is worth 0.10
    total_nickels = 9 * 10 * 0.05  # 9 piles of nickels, 10 coins per pile, each nickel is worth 0.05
    total_pennies = 5 * 10 * 0.01  # 5 piles of pennies, 10 coins per pile, each penny is worth 0.01
    total_money = total_quarters + total_dimes + total_nickels + total_pennies
    result = total_money
    return result

print(solution())