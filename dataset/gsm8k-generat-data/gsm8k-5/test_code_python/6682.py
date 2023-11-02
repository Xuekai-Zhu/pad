def solution():
    # Beth had 125 gold coins
    initial_coins = 125

    # Carl gave Beth 35 more gold coins
    gift_coins = 35

    # Total number of coins after the gift
    total_coins = initial_coins + gift_coins

    # Beth decided to sell half of her coins
    sold_coins = total_coins / 2

    result = sold_coins
    return result

print(solution())