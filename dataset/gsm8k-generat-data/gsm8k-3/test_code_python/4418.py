def solution():
    """Tim spent $50.00 on Chinese take-out.  80% of the cost went to 4 entrees.  The rest of the money went to 2 appetizers that each cost the same amount.  How much was the price of a single appetizer?"""
    # Calculate the cost of the entrees
    entree_cost = 50 * 0.8
    entree_each_cost = entree_cost / 4

    # Calculate the cost of the appetizers
    appetizer_cost = 50 - entree_cost
    appetizer_each_cost = appetizer_cost / 2

    # Display the cost of a single appetizer
    result = appetizer_each_cost
    return result

print(solution())