def solution():
    budget = 260  # Sophie has $260 to spend on clothes
    shirts_cost = 18.5 * 2  # she buys 2 shirts at $18.50 each
    trousers_cost = 63  # she buys a pair of trousers that cost $63
    remaining_budget = budget - shirts_cost - trousers_cost  # she has this much money left for 4 more items
    num_of_items = 4  # she buys 4 more items with her remaining budget

    # Calculate the total cost of the 4 items Sophie buys with her remaining budget
    total_items_cost = remaining_budget / num_of_items

    # Calculate the cost per item if Sophie splits the cost evenly
    cost_per_item = total_items_cost / num_of_items
    result = cost_per_item
    return result

print(solution())