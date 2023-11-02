def solution():
    # Calculate the profit a restaurant makes on a bottle of spirits
    cost_per_serving = 30.00/16  # cost per serving
    profit_per_serving = 8.00 - cost_per_serving  # profit per serving
    total_profit = profit_per_serving * 16  # total profit from selling 16 servings in one bottle
    result = total_profit
    return result

print(solution())