def solution():
    # Define the cost and number of servings per bottle
    bottle_cost = 30.00
    servings_per_bottle = 16

    # Calculate the revenue from selling one serving
    serving_revenue = 8.00

    # Calculate the total revenue from selling all servings in one bottle
    total_revenue = servings_per_bottle * serving_revenue

    # Calculate the profit made on one bottle of spirits
    profit = total_revenue - bottle_cost

    result = profit
    return result

print(solution())