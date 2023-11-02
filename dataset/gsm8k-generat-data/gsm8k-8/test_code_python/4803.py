def solution():
    # Calculate the total cost of ingredients
    apple_cost = 2 * 2  # 2 pounds of apples at $2.00 per pound
    crust_cost = 2.00
    lemon_cost = 0.50
    butter_cost = 1.50
    total_cost = apple_cost + crust_cost + lemon_cost + butter_cost

    # Calculate the cost per serving
    servings = 8
    cost_per_serving = total_cost / servings

    result = cost_per_serving
    return result

print(solution())