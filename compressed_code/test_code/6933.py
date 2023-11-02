def solution():
    
    appetizer_cost = 10
    entree_cost = 20
    num_entrees = 4
    subtotal = appetizer_cost + (entree_cost * num_entrees)
    tip_percent = 20
    tip_amount = subtotal * (tip_percent / 100)
    total_cost = subtotal + tip_amount
    result = total_cost
    return result

print(solution())