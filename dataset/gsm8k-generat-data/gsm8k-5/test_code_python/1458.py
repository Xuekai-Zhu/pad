def solution():
    appetizer_cost = 10
    entree_cost = 20
    num_entrees = 4

    # Calculate total cost of entrees
    entree_total = entree_cost * num_entrees

    # Calculate subtotal before tip
    subtotal = appetizer_cost + entree_total

    # Calculate tip amount
    tip_percent = 0.2
    tip_amount = subtotal * tip_percent

    # Calculate total cost including tip
    total_cost = subtotal + tip_amount
    result = total_cost
    return result

print(solution())