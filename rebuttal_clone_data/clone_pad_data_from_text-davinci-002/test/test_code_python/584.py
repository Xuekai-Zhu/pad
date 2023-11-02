def solution():
    cost_per_orange = 1.20
    calories_per_orange = 80
    money_available = 10
    target_calories = 400
    number_of_oranges = target_calories / calories_per_orange
    total_cost = cost_per_orange * number_of_oranges
    money_left = money_available - total_cost
    result = money_left
    return result

print(solution())