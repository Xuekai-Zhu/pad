def solution():
    """James buys 20 coins of a cryptocurrency at $15 each. The value of the coins increases by 2/3. He sells coins to recoup his original investment. How many coins did he sell?"""
    num_coins = 20
    cost_per_coin = 15
    increase_percent = 2/3
    increase_amount = cost_per_coin * increase_percent
    new_value = cost_per_coin + increase_amount
    total_value = num_coins * new_value
    original_investment = num_coins * cost_per_coin
    coins_sold = (total_value - original_investment) / new_value
    result = coins_sold
    return result

print(solution())