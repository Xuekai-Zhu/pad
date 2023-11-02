def solution():
    """Oranges have 80 calories and cost $1.20 each. If Timmy has $10 and needs to make sure he gets 400 calories, how much money will he have left after he buys the oranges he needs?"""
    orange_calories = 80
    orange_cost = 1.20
    desired_calories = 400
    budget = 10
    num_oranges = desired_calories // orange_calories
    cost = num_oranges * orange_cost
    remaining_budget = budget - cost
    result = remaining_budget
    return result

print(solution())