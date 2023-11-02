def solution():
    """Frank spent 1/5 of his money to buy groceries. He then spent 1/4 of the remaining money to buy a magazine. If he had $360 left in his wallet, how much money did he have at first?"""
    remaining_money = 360
    magazine_cost = remaining_money * 0.25
    remaining_money -= magazine_cost
    grocery_cost = remaining_money * 0.2
    remaining_money -= grocery_cost
    initial_money = remaining_money / 0.6  # the remaining money is 0.6 of initial money
    result = initial_money
    return result

print(solution())