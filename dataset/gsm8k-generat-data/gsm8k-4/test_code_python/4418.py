def solution():
    """Tim spent $50.00 on Chinese take-out. 80% of the cost went to 4 entrees. The rest of the money went to 2 appetizers that each cost the same amount. How much was the price of a single appetizer?"""
    # Define the total cost and the cost of the entrees
    total_cost = 50
    entree_cost = total_cost * 0.8

    # Calculate the cost of a single entree
    single_entree_cost = entree_cost / 4

    # Calculate the cost of the appetizers
    appetizer_cost = total_cost - entree_cost

    # Calculate the cost of a single appetizer
    single_appetizer_cost = appetizer_cost / 2

    result = single_appetizer_cost
    return result

print(solution())