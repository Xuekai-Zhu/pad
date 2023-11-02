def solution():
    appetizer_cost = 10
    num_entrees = 4
    entree_cost = 20
    tip_percent = 0.2  # 20% tip

    # Calculate the total cost of all entrees
    total_entree_cost = num_entrees * entree_cost

    # Calculate the subtotal before tip
    subtotal = appetizer_cost + total_entree_cost

    # Calculate the total cost including tip
    total_cost = subtotal * (1 + tip_percent)
    result = total_cost
    return result

print(solution())