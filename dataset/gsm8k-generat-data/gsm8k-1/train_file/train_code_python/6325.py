def solution():
    """Ali has $480. He spent half of it on food, and then he spent a third of what was left on a pair of glasses. How much money did he have left?"""
    initial_money = 480
    spent_on_food = initial_money / 2
    money_left = initial_money - spent_on_food
    spent_on_glasses = money_left / 3
    money_left -= spent_on_glasses
    result = money_left
    return result

print(solution())