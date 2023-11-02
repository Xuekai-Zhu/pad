def solution():
    game_cost = 60
    ice_cream_price = 5
    total_money_needed = game_cost

    money_raised = 0
    ice_creams_sold = 0
    
    while money_raised < total_money_needed:
        money_raised += ice_cream_price
        ice_creams_sold += 1

    result = ice_creams_sold
    return result

print(solution())