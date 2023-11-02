def solution():
    # Calculate the cost of the entrees
    entree_cost = 50 * 0.8 / 4

    # Calculate the total cost of the appetizers
    appetizer_cost = 50 - (entree_cost * 4)

    # Calculate the cost of a single appetizer
    single_appetizer_cost = appetizer_cost / 2
    result = single_appetizer_cost
    return result

print(solution())