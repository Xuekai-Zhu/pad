def solution():
    initial_money = 10
    money_spent_on_cupcakes = initial_money / 5
    money_left = initial_money - money_spent_on_cupcakes
    money_spent_on_milkshake = money_left - 3
    result = money_spent_on_milkshake
    
    return result

print(solution())