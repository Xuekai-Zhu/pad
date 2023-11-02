def solution():
    # Define variables
    starting_gold = 20
    sold_gold = 3
    remaining_gold = starting_gold - sold_gold
    money_after_sale = 12
    price_per_coin = (starting_gold - money_after_sale) / sold_gold

    # Calculate gold coins remaining
    remaining_coins = remaining_gold / price_per_coin
    result = remaining_coins
    return result

print(solution())