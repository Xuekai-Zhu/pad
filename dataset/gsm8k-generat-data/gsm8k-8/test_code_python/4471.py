def solution():
    # Calculate the total cost of the items in Alice's cart
    chicken_cost = 6 * 1.5
    lettuce_cost = 3
    tomato_cost = 2.5
    sweet_potato_cost = 4 * 0.75
    broccoli_cost = 2 * 2
    brussel_sprouts_cost = 2.5
    total_cost = chicken_cost + lettuce_cost + tomato_cost + sweet_potato_cost + broccoli_cost + brussel_sprouts_cost

    # Calculate the amount Alice needs to spend to get free delivery
    free_delivery_amount = 35

    # Calculate how much more Alice needs to spend
    more_to_spend = free_delivery_amount - total_cost

    result = more_to_spend
    return result

print(solution())