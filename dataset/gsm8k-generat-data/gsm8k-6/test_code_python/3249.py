def solution():
    # Calculate the cost of 5 pounds of strawberries
    cost_strawberries = 2.20 * 5

    # Calculate the cost of 5 pounds of cherries (6 times the cost of strawberries)
    cost_cherries = 6 * cost_strawberries

    # Calculate the total cost of the strawberries and cherries
    total_cost = cost_strawberries + cost_cherries
    result = total_cost
    return result

print(solution())