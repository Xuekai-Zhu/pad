def solution():
    """You have 32$ to spend on groceries. You buy a loaf of bread for 3$, a candy bar for 2$, and 1/3 of whats left on a Turkey. How much money do you have left?"""
    money_spent_on_bread = 3
    money_spent_on_candy = 2
    total_money_spent_on_food = money_spent_on_bread + money_spent_on_candy
    money_left_for_turkey = 32 - total_money_spent_on_food
    money_spent_on_turkey = money_left_for_turkey / 3
    money_left = 32 - (total_money_spent_on_food + money_spent_on_turkey)
    result = money_left
    return result

print(solution())