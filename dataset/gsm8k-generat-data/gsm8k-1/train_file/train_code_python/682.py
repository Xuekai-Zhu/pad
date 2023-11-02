def solution():
    """Julia has $40. She spends half of her money to buy a new game for her phone. She spends a quarter of what she has left on in-game purchases. How much money does she have left?"""
    starting_money = 40
    game_cost = starting_money / 2
    remaining_money = starting_money - game_cost
    in_game_cost = remaining_money / 4
    money_left = remaining_money - in_game_cost
    result = money_left
    return result

print(solution())