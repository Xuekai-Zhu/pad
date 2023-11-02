def solution():
    cost_strawberries = 2.20  # A pound of strawberries costs $2.20
    cost_cherries = 6 * cost_strawberries  # A pound of cherries costs 6 times as much as strawberries
    pounds_strawberries = 5  # Briget will buy 5 pounds of strawberries
    pounds_cherries = 5  # Briget will also buy 5 pounds of cherries

    # Calculate the total cost of strawberries and cherries
    total_cost = (cost_strawberries * pounds_strawberries) + (cost_cherries * pounds_cherries)
    result = total_cost
    return result

print(solution())