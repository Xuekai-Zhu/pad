def solution():
    
    initial_budget = 260
    shirts_cost = 2 * 18.5
    trousers_cost = 63
    remaining_budget = initial_budget - shirts_cost - trousers_cost
    num_items = 4
    each_item_cost = remaining_budget / num_items
    result = each_item_cost
    return result

print(solution())