def solution():
    
    appetizer_cost = 10
    entree_cost = 20
    num_entrees = 4
    meal_cost = appetizer_cost + (entree_cost * num_entrees)
    tip_percent = 0.2
    tip_amount = meal_cost * tip_percent
    total_cost = meal_cost + tip_amount
    result = total_cost
    return result

print(solution())