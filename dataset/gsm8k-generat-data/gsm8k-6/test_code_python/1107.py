def solution():
    # Find the cost of one gold coin
    cost_one_coin = (20 - 12) / 3  # Roman had $20 before and $12 after selling 3 coins

    # Find the number of gold coins Roman has left
    coins_left = round((20 - cost_one_coin) / cost_one_coin)  # round to nearest integer
    result = coins_left
    return result

print(solution())