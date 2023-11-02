def solution():
    """Beth had a set of 125 gold coins. Carl gave Beth a gift of an additional 35 gold coins. Then, Beth decided to sell half of her coins. How many coins did Beth sell?"""
    initial_coins = 125
    gift_coins = 35
    total_coins = initial_coins + gift_coins
    coins_to_sell = total_coins / 2
    result = coins_to_sell
    return result

print(solution())