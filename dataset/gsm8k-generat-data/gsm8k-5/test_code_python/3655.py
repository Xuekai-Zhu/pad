def solution():
    cheese_weight = 1.5  # Martha needs 1.5 kilograms of cheese
    meat_weight = 0.5  # Martha needs 0.5 kilograms of meat
    cheese_cost = 6  # The cost of cheese is $6 per kilogram
    meat_cost = 8  # The cost of meat is $8 per kilogram

    # Calculate the total cost of cheese and meat
    cheese_cost_total = cheese_weight * cheese_cost
    meat_cost_total = meat_weight * meat_cost
    total_cost = cheese_cost_total + meat_cost_total
    result = total_cost
    return result

print(solution())