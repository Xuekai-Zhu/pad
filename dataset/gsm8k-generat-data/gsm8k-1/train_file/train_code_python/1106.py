def solution():
    """Roman the Tavernmaster has $20 worth of gold coins. He sells 3 gold coins to Dorothy. After she pays him, he has $12. How many gold coins does Roman have left?"""
    initial_value = 20
    sold_coins = 3
    remaining_value = 12
    value_per_coin = initial_value / (initial_value // sold_coins)
    remaining_coins = (remaining_value / value_per_coin) - sold_coins
    result = remaining_coins
    return result

print(solution())