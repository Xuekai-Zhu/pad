def solution():
    min_spend = 35.0
    chicken_weight = 1.5
    chicken_price_per_lb = 6.0
    lettuce_price = 3.0
    cherry_tomatoes_price = 2.5
    sweet_potatoes_num = 4
    sweet_potatoes_price = 0.75
    broccoli_num = 2
    broccoli_price = 2.0
    brussel_sprouts_weight = 1.0
    brussel_sprouts_price = 2.5

    # Calculate the total cost of all items in Alice's cart
    chicken_cost = chicken_weight * chicken_price_per_lb
    lettuce_cost = lettuce_price
    cherry_tomatoes_cost = cherry_tomatoes_price
    sweet_potatoes_cost = sweet_potatoes_num * sweet_potatoes_price
    broccoli_cost = broccoli_num * broccoli_price
    brussel_sprouts_cost = brussel_sprouts_weight * brussel_sprouts_price

    total_cost = chicken_cost + lettuce_cost + cherry_tomatoes_cost + sweet_potatoes_cost + broccoli_cost + brussel_sprouts_cost

    # Calculate how much more Alice needs to spend to reach the minimum for free delivery
    additional_spend = max(0, min_spend - total_cost)
    result = additional_spend
    return result

print(solution())