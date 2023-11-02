def solution():
    total_cost = 50.0
    entrees_cost = 0.8 * total_cost
    num_entrees = 4
    entree_price = entrees_cost / num_entrees

    # Calculate the cost of the 2 appetizers
    appetizer_cost = total_cost - entrees_cost
    num_appetizers = 2

    # Divide the remaining cost by the number of appetizers to get the price of a single appetizer
    appetizer_price = appetizer_cost / (num_appetizers * 1.0)
    result = appetizer_price
    return result

print(solution())