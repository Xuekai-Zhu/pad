def solution():
    """Darwin has 600$. He spent 1/3 of it on gas for his car, and 1/4 of what was left on food. How much money did he have left?"""
    starting_money = 600
    gas_spending = starting_money / 3
    money_left = starting_money - gas_spending
    food_spending = money_left / 4
    money_left -= food_spending
    result = money_left
    return result

print(solution())