def solution():
    cheese_weight = 8
    cheese_price_per_kg = 4
    veggie_weight = 7
    veggie_price_per_kg = cheese_price_per_kg + 2

    # Calculate the total cost of all cheese
    cheese_cost = cheese_weight * cheese_price_per_kg

    # Calculate the total cost of all vegetables
    veggie_cost = veggie_weight * veggie_price_per_kg

    # Calculate the total cost of Emma's shopping
    total_cost = cheese_cost + veggie_cost
    result = total_cost
    return result

print(solution())