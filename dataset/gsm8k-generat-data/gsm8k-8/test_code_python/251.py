def solution():
    # Calculate the cost of producing one pie
    pie_cost = 0.5 + (3 * 4)

    # Calculate the revenue of selling one pie
    pie_revenue = 3 * 4

    # Calculate the profit of selling one pie
    pie_profit = pie_revenue - pie_cost

    # Calculate the total profit of making 12 pies
    total_profit = pie_profit * 12

    result = total_profit
    return result

print(solution())