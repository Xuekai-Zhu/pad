def solution():
    initial_gold_value = 20
    sold_gold_coins = 3
    remaining_gold_value = 12

    # Calculate the value of one gold coin
    coin_value = initial_gold_value / (initial_gold_value // sold_gold_coins)

    # Calculate the number of gold coins Roman had initially
    initial_gold_coins = initial_gold_value / coin_value

    # Calculate the number of gold coins Roman has left
    remaining_gold_coins = initial_gold_coins - sold_gold_coins

    result = remaining_gold_coins
    return result

print(solution())