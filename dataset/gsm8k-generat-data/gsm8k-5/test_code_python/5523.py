def solution():
    game_cost = 50  # Joe spends $50 a month on video games
    game_sell_price = 30  # Joe sells his games for $30 each
    starting_money = 240  # Joe starts with $240
    games_bought = 0  # Keep track of how many games Joe buys

    while starting_money >= game_cost:
        starting_money -= game_cost  # Joe spends money on a new game
        starting_money += game_sell_price  # Joe sells a used game
        games_bought += 1

    result = games_bought
    return result

print(solution())