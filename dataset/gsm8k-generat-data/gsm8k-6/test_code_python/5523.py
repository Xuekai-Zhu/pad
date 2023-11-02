def solution():
    # Calculate the number of games Joe can buy and sell
    total_money = 240
    cost_per_month = 50
    selling_price = 30
    num_games = 0
    while total_money >= cost_per_month:
        num_games += 1
        total_money -= cost_per_month
        total_money += selling_price
    result = num_games
    return result

print(solution())