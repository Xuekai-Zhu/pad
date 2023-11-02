def solution():
    
    starting_money = 40
    game_cost = starting_money / 2
    remaining_money = starting_money - game_cost
    in_game_cost = remaining_money / 4
    money_left = remaining_money - in_game_cost
    result = money_left
    return result

print(solution())