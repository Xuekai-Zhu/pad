def solution():
    # Define the initial number of coins and the gift
    initial_coins = 125
    gift_coins = 35

    # Calculate the total number of coins after the gift
    total_coins = initial_coins + gift_coins

    # Calculate the number of coins sold (half of the total number)
    sold_coins = total_coins / 2

    result = sold_coins
    return result

print(solution())