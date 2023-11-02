def solution():
    items_bought = 7
    cost_per_item = 200
    discount = 10
    total_cost = items_bought * cost_per_item
    total_cost_discount = total_cost - ((discount / 100) * total_cost)
    result = total_cost_discount
    return result

print(solution())