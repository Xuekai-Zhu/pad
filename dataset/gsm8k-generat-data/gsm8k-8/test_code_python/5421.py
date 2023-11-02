def solution():
    # Define the total spent and the difference in cost between the entree and dessert
    total_spent = 23
    entree_diff = 5

    # Set up equations to solve for the cost of the entree and dessert
    entree_cost = (total_spent + entree_diff) / 2
    dessert_cost = entree_cost - entree_diff

    result = entree_cost
    return result

print(solution())