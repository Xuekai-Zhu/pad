def solution():
    chicken_cost = 6 * 1.5  # Cost of 1.5 pounds of chicken at $6.00 per pound
    lettuce_cost = 3  # Cost of 1 pack of lettuce for $3.00
    tomatoes_cost = 2.5  # Cost of cherry tomatoes for $2.50
    potatoes_cost = 4 * 0.75  # Cost of 4 sweet potatoes at $0.75 each
    broccoli_cost = 2 * 2  # Cost of 2 heads of broccoli for $2.00 each
    sprouts_cost = 2.5  # Cost of 1 pound of Brussel sprouts for $2.50

    # Calculate the total cost of the items in Alice's cart
    total_cost = chicken_cost + lettuce_cost + tomatoes_cost + potatoes_cost + broccoli_cost + sprouts_cost

    # Calculate the amount Alice needs to spend to get free delivery
    remaining_cost = 35 - total_cost
    result = remaining_cost
    return result

print(solution())