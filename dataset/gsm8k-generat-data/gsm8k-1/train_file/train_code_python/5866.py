def solution():
    """Sophie's aunt gave her $260 to spend on clothes at the mall. She bought 2 shirts that cost $18.50 each and a pair of trousers that cost $63. She then decides to purchase 4 more articles of clothing with her remaining budget. How much money would each item cost if she split the cost of each item evenly?"""
    initial_budget = 260
    shirt_cost = 18.5
    trouser_cost = 63
    remaining_budget = initial_budget - (2 * shirt_cost) - trouser_cost
    num_items = 4
    cost_per_item = remaining_budget / num_items
    result = cost_per_item
    return result

print(solution())