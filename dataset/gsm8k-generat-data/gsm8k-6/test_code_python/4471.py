def solution():
    # Calculate the total cost of items in Alice's cart
    chicken_cost = 1.5 * 6.00
    lettuce_cost = 3.00
    tomatoes_cost = 2.50
    sweet_potatoes_cost = 4 * 0.75
    broccoli_cost = 2 * 2.00
    brussel_sprouts_cost = 2.50
    total_cost = chicken_cost + lettuce_cost + tomatoes_cost + sweet_potatoes_cost + broccoli_cost + brussel_sprouts_cost

    # Calculate the amount Alice needs to spend to qualify for free delivery
    remaining_cost = 35.00 - total_cost
    result = remaining_cost
    return result

print(solution())