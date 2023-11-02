def solution():
    sandwich_price = 1.5
    bread_price = 0.15
    ham_price = 0.25
    cheese_price = 0.35

    # Calculate the cost of the sandwich ingredients
    total_cost = bread_price + ham_price + cheese_price

    # Convert the total cost to cents
    cost_in_cents = total_cost * 100

    result = cost_in_cents
    return result

print(solution())