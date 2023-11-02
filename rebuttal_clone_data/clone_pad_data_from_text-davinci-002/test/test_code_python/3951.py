def solution():
    initial_money = 600
    spent_on_gas = initial_money / 3
    money_left = initial_money - spent_on_gas
    spent_on_food = money_left / 4
    result = money_left - spent_on_food
    return result

print(solution())