def solution():
    initial_coins = 125
    gift_coins = 35

    # Calculate the total number of coins Beth has now
    total_coins = initial_coins + gift_coins

    # Calculate the number of coins that Beth will sell
    coins_to_sell = total_coins / 2 - gift_coins

    result = coins_to_sell
    return result

print(solution())