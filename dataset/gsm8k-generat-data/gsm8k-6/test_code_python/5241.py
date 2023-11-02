def solution():
    # Find the cost of one chocolate-dipped strawberry
    cost_per_strawberry = 50 / 12  # $50 a dozen

    # Find the revenue of selling half a dozen chocolate-dipped strawberries
    revenue_per_half_dozen = 30  # $30 for half a dozen
    revenue_per_strawberry = revenue_per_half_dozen / 3  # $30 for half a dozen is $10 for one strawberry

    # Calculate the profit per strawberry
    profit_per_strawberry = revenue_per_strawberry - cost_per_strawberry

    # Find the total profit of selling 50 dozens
    dozens_sold = 50
    strawberries_sold = dozens_sold * 12
    total_profit = profit_per_strawberry * strawberries_sold

    result = total_profit
    return result

print(solution())