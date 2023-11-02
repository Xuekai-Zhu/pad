def solution():
    pasta_cost = 1.0
    sauce_cost = 2.0
    meatballs_cost = 5.0
    num_servings = 8

    # Calculate the total cost of all ingredients
    total_cost = pasta_cost + sauce_cost + meatballs_cost

    # Calculate the cost per serving
    cost_per_serving = total_cost / num_servings
    result = cost_per_serving
    return result

print(solution())