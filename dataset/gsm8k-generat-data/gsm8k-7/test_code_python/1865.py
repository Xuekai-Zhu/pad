def solution():
    # Linda's original coins
    num_dimes = 2
    num_quarters = 6
    num_nickels = 5

    # Coins given by Linda's mother
    num_dimes_mother = 2
    num_quarters_mother = 10
    num_nickels_mother = num_nickels * 2

    # Calculate the total number of coins
    total_coins = num_dimes + num_quarters + num_nickels + num_dimes_mother + num_quarters_mother + num_nickels_mother

    result = total_coins
    return result

print(solution())