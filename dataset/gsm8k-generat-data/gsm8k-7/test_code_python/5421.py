def solution():
    total_cost = 23
    entree_cost_diff = 5
    
    # Assume dessert cost = x
    # Then entree cost = x + entree_cost_diff
    # Total cost = dessert cost + entree cost = x + (x + entree_cost_diff) = 2x + entree_cost_diff
    # Solve for x: 2x + entree_cost_diff = total_cost
    # x = (total_cost - entree_cost_diff) / 2
    dessert_cost = (total_cost - entree_cost_diff) / 2
    entree_cost = dessert_cost + entree_cost_diff
    result = entree_cost
    return result

print(solution())