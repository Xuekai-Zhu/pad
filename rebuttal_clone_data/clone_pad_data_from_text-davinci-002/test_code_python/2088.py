def solution():
    pasta_cost = 1
    sauce_cost = 2
    meatball_cost = 5
    total_servings = 8
    total_cost = (pasta_cost + sauce_cost + meatball_cost) * total_servings
    cost_per_serving = total_cost / total_servings
    result = cost_per_serving
    return result

print(solution())