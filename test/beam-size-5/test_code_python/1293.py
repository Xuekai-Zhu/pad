def solution():
    # Calculate the cost of passion fruit and jackfruit
    cost_passion_fruit = 2 * 6  # 2 pounds of passion fruit at $6 per pound
    cost_jackfruit = 1.5 * 8  # 1.5 pounds of jackfruit at $8 per pound
    cost_honey = 2 * 10  # 2 pounds of special honey at $10 per pound
    total_cost = cost_passion_fruit + cost_jackfruit + cost_honey

    # Calculate the profit made from selling 10 jars
    profit = total_cost - 50  # Tim sells each jar for $50
    result = profit
    return result

print(solution())