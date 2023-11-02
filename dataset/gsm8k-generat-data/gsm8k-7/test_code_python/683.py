def solution():
    initial_money = 40

    # Calculate how much money Julia spends on the new game
    game_cost = initial_money / 2

    # Calculate how much money Julia has left after buying the new game
    remaining_money = initial_money - game_cost

    # Calculate how much money Julia spends on in-game purchases
    in_game_purchases = remaining_money / 4

    # Calculate how much money Julia has left after buying the in-game purchases
    money_left = remaining_money - in_game_purchases
    result = money_left
    return result

print(solution())