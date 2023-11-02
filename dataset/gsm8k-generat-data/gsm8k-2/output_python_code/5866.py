def solution():
    """Sophie's aunt gave her $260 to spend on clothes at the mall. She bought 2 shirts that cost $18.50 each and a pair of trousers that cost $63. She then decides to purchase 4 more articles of clothing with her remaining budget. How much money would each item cost if she split the cost of each item evenly?"""
    initial_budget = 260
    shirts_cost = 2 * 18.5
    trousers_cost = 63
    remaining_budget = initial_budget - shirts_cost - trousers_cost
    num_items = 4
    each_item_cost = remaining_budget / num_items
    result = each_item_cost
    return result

print(solution())