def solution():
    hamburger_weight = 2
    hamburger_price = 3.5
    bun_price = 1.5
    lettuce_price = 1.0
    tomato_weight = 1.5
    tomato_price = 2.0
    pickle_price = 2.5
    pickle_discount = 1
    total_cost = (hamburger_weight * hamburger_price) + bun_price + lettuce_price + (tomato_weight * tomato_price) + (pickle_price - pickle_discount)
    change = 20 - total_cost
    result = change
    return result

print(solution())