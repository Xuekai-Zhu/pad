def solution():
    """Darwin has 600$. He spent 1/3 of it on gas for his car,
    and 1/4 of what was left on food. How much money did he have left?"""
    initial_money = 600
    gas_cost = initial_money / 3
    money_left = initial_money - gas_cost
    food_cost = money_left / 4
    money_left = money_left - food_cost
    result = money_left
    return result

print(solution())