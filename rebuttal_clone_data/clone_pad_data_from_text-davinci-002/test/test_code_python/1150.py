def solution():
    saved_money = 400
    money_spent_on_supplies = saved_money / 4
    money_left = saved_money - money_spent_on_supplies
    money_spent_on_food = money_left / 2
    money_left = money_left - money_spent_on_food
    result = money_left
    return result

print(solution())