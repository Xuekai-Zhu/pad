def solution():
    
    starting_money = 40
    game_cost = starting_money / 2
    remaining_money = starting_money - game_cost
    in_game_purchase_cost = remaining_money / 4
    final_money = remaining_money - in_game_purchase_cost
    result = final_money
    return result

print(solution())