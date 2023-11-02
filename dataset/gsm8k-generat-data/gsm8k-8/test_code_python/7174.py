def solution():
    initial_money = 65
    ice_cream_cost = 5
    remaining_money = initial_money - ice_cream_cost
    tshirt_cost = remaining_money / 2
    remaining_money -= tshirt_cost
    deposited_money = remaining_money / 5
    remaining_money -= deposited_money
    result = remaining_money
    return result

print(solution())