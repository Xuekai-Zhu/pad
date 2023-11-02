def solution():
    # Calculate the amount of money Randy has left after buying lunch
    remaining_money = 30 - 10  # Randy had $30 and spent $10 on lunch
    ice_cream_cost = remaining_money / 4  # Randy spent a quarter of his remaining money on an ice cream cone
    money_left = remaining_money - ice_cream_cost  # Randy has this much money left
    result = money_left
    return result

print(solution())