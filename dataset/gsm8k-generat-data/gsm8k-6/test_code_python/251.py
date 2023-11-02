def solution():
    # Calculate the cost of creating one pie
    pie_cost = 0.5 + (4 * 3)  # Cost of ingredients and labor for one pie

    # Calculate the revenue from selling one pie
    pie_revenue = 4 * 3  # Revenue from selling three pieces of one pie

    # Calculate the profit per pie
    pie_profit = pie_revenue - pie_cost

    # Calculate the total profit for 12 pies
    total_profit = 12 * pie_profit

    result = total_profit
    return result

print(solution())