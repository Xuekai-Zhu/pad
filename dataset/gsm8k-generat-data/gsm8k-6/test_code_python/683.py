def solution():
    # Calculate how much Julia spends on the game
    game_cost = 40 / 2
    left_after_game = 40 - game_cost

    # Calculate how much Julia spends on in-game purchases
    in_game_cost = left_after_game / 4
    money_left = left_after_game - in_game_cost

    result = money_left
    return result

print(solution())