def solution():
    # Define the number of quarters, dimes, and nickels Emerie has
    emerie_quarters = 6
    emerie_dimes = 7
    emerie_nickels = 5

    # Calculate the number of coins Zain has using the fact that he has 10 more of each coin than Emerie
    zain_quarters = emerie_quarters + 10
    zain_dimes = emerie_dimes + 10
    zain_nickels = emerie_nickels + 10

    # Calculate the total number of coins Zain has
    total_coins = zain_quarters + zain_dimes + zain_nickels
    result = total_coins
    return result

print(solution())