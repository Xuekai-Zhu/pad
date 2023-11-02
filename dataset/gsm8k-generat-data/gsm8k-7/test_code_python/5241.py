def solution():
    cost_per_dozen = 50
    selling_price_per_half_dozen = 30
    num_dozens_sold = 50

    # Calculate the cost of one chocolate-dipped strawberry
    cost_per_strawberry = cost_per_dozen / 12

    # Calculate the selling price of one chocolate-dipped strawberry
    selling_price_per_strawberry = selling_price_per_half_dozen / 6

    # Calculate the profit per strawberry
    profit_per_strawberry = selling_price_per_strawberry - cost_per_strawberry

    # Calculate the profit per dozen
    profit_per_dozen = profit_per_strawberry * 12

    # Calculate the total profit for selling 50 dozens
    total_profit = profit_per_dozen * num_dozens_sold
    result = total_profit
    return result

print(solution())