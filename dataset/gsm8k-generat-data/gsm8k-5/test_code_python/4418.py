def solution():
    total_cost = 50.0  # Tim spent $50.00 on Chinese take-out
    entree_cost = (80/100) * total_cost / 4  # 80% of the cost went to 4 entrees
    remaining_cost = total_cost - ((80/100) * total_cost)  # The rest of the money went to 2 appetizers
    appetizer_cost = remaining_cost / 2  # The 2 appetizers cost the same amount

    # Calculate the price of a single appetizer
    price_of_single_appetizer = appetizer_cost / 1
    result = price_of_single_appetizer
    return result

print(solution())