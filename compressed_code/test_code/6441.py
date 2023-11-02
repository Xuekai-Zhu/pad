def solution():
    
    starting_money = 30
    lunch_cost = 10
    money_left = starting_money - lunch_cost
    ice_cream_cost = money_left / 4
    money_left -= ice_cream_cost
    result = money_left
    return result

print(solution())