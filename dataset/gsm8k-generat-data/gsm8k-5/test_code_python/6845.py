def solution():
    # Calculate the cost per apple and per orange
    cost_per_apple = 3/2  # 2 apples for $3
    cost_per_orange = 2.70/3  # 3 oranges for $2.70

    # Calculate the revenue from selling 5 apples and 5 oranges
    revenue_apples = (10/5) * 5  # 5 apples for $10
    revenue_oranges = 1 * 5  # Sell 5 oranges for $1 each
    total_revenue = revenue_apples + revenue_oranges

    # Calculate the cost of the apples and oranges
    cost_apples = cost_per_apple * 5
    cost_oranges = cost_per_orange * 5
    total_cost = cost_apples + cost_oranges

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())