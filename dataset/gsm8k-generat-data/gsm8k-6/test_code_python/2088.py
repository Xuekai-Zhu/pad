def solution():
    # Calculate the total cost of ingredients
    pasta_cost = 1.00
    sauce_cost = 2.00
    meatball_cost = 5.00
    total_cost = pasta_cost + sauce_cost + meatball_cost

    # Calculate the cost per serving
    servings = 8
    cost_per_serving = total_cost / servings
    result = cost_per_serving
    return result

print(solution())