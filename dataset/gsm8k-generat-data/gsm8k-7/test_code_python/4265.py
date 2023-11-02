def solution():
    emerie_quarters = 6
    emerie_dimes = 7
    emerie_nickels = 5

    # Calculate the total number of coins that Emerie has
    emerie_coins = emerie_quarters + emerie_dimes + emerie_nickels

    # Calculate the total number of coins that Zain has
    zain_coins = emerie_coins + 30  # 10 more of each coin than Emerie

    result = zain_coins
    return result

print(solution())