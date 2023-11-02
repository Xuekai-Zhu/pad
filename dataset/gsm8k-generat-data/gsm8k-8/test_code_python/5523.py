def solution():
    # Initialize variables
    starting_money = 240
    game_cost = 50
    game_sell_price = 30
    num_months = 0

    # Keep buying and selling games until Joe runs out of money
    while starting_money >= game_cost:
        num_months += 1
        starting_money -= game_cost
        starting_money += game_sell_price

    result = num_months
    return result

print(solution())