def solution():
    
    appetizer_cost = 9
    entree_cost = 20
    dessert_cost = 11
    subtotal = (appetizer_cost + (2 * entree_cost) + dessert_cost)
    tip_percent = 30
    tip = subtotal * (tip_percent / 100)
    total_cost = subtotal + tip
    result = total_cost
    return result

print(solution())