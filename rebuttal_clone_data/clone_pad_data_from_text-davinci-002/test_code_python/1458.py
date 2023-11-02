def solution():
    appetizer_cost = 10
    entree_cost = 20
    num_entrees = 4
    total_cost = appetizer_cost + (entree_cost * num_entrees)
    tip_percent = 20
    tip_amount = total_cost * (tip_percent / 100)
    total_spent = total_cost + tip_amount
    result = total_spent
    
    return result

print(solution())