def solution():
    items_in_cart = 28
    cost_of_items = 10
    total_cost = items_in_cart * cost_of_items
    teddy_bears = 20
    money_available = 580
    cost_of_teddy_bears = (money_available - total_cost) / teddy_bears
    result = cost_of_teddy_bears
    return result

print(solution())