def solution():
    sandwich_price = 2
    hamburger_price = 2
    hotdog_price = 1
    juice_price = 2

    # Selene's order
    selene_sandwiches = 3
    selene_juice = 1
    selene_cost = selene_sandwiches * sandwich_price + selene_juice * juice_price

    # Tanya's order
    tanya_hamburgers = 2
    tanya_juice = 2
    tanya_cost = tanya_hamburgers * hamburger_price + tanya_juice * juice_price

    # Calculate the total cost of both orders
    total_cost = selene_cost + tanya_cost
    result = total_cost
    return result

print(solution())