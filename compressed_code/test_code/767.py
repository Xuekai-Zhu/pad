def solution():
    
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