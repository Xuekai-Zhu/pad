def solution():
    burger_cost = 3.20 * 2
    fry_cost = 1.90 * 2
    milkshake_cost = 2.40 * 2
    order_total = burger_cost + fry_cost + milkshake_cost
    minimum_order = 18
    amount_needed = minimum_order - order_total
    result = amount_needed
    return result

print(solution())