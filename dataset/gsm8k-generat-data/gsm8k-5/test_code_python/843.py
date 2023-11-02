def solution():
    initial_money = 30  # Randy has $30
    lunch_cost = 10  # Randy spent $10 on lunch
    money_left = initial_money - lunch_cost  # Randy has this much money left
    ice_cream_cost = money_left / 4  # Randy spent a quarter of the money he had left on an ice cream cone
    money_left -= ice_cream_cost  # Randy now has this much money left after buying the ice cream cone
    result = money_left
    return result

print(solution())