def solution():
    cheese_amount = 1.5 # kg
    cheese_cost_per_kg = 6 # $
    meat_amount = 0.5 # kg
    meat_cost_per_kg = 8 # $

    # Calculate the total cost of cheese
    cheese_cost = cheese_amount * cheese_cost_per_kg

    # Calculate the total cost of meat
    meat_cost = meat_amount * meat_cost_per_kg

    # Calculate the total cost of all ingredients
    total_cost = cheese_cost + meat_cost
    result = total_cost
    return result

print(solution())