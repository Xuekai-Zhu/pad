def solution():
    
    initial_money = 30
    lunch_cost = 10
    remaining_money = initial_money - lunch_cost
    ice_cream_cost = remaining_money / 4
    final_money = remaining_money - ice_cream_cost
    result = final_money
    return result

print(solution())