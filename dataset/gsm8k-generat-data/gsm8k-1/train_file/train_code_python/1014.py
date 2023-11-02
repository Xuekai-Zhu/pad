def solution():
    """Oranges have 80 calories and cost $1.20 each. If Timmy has $10 and needs to make sure he gets 400 calories, how much money will he have left after he buys the oranges he needs?"""
    calories_per_orange = 80
    cost_per_orange = 1.20
    total_calories_needed = 400
    oranges_needed = total_calories_needed / calories_per_orange
    cost_of_oranges = oranges_needed * cost_per_orange
    money_left = 10 - cost_of_oranges
    result = money_left
    return result

print(solution())