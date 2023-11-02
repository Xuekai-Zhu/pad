def solution():
    """Tim spent $50.00 on Chinese take-out. 80% of the cost went to 4 entrees. The rest of the money went to 2 appetizers that each cost the same amount. How much was the price of a single appetizer?"""
    total_cost = 50
    entree_cost = total_cost * 0.8 / 4
    appetizer_cost = (total_cost - entree_cost * 4) / 2
    result = appetizer_cost
    return result

print(solution())