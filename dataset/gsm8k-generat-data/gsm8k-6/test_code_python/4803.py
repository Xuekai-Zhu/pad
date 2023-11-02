def solution():
    # Calculate the total cost of ingredients
    cost_apples = 2 * 2  # 2 pounds of apples at $2.00 per pound
    cost_pie_crust = 2.00
    cost_lemon = 0.50
    cost_butter = 1.50
    total_cost = cost_apples + cost_pie_crust + cost_lemon + cost_butter

    # Calculate the cost per serving of pie
    cost_per_serving = total_cost / 8
    result = cost_per_serving
    return result

print(solution())