def solution():
    """A vendor bought apples at 2 for $3 and plans to sell them at 5 for $10. He also bought 3 oranges for $2.70 and plans to sell them at $1 each.
    How much is his profit if he sells 5 apples and 5 oranges?"""
    num_apples_bought = 4  # 2 for $3, so 4 for $6
    num_oranges_bought = 3
    cost_apples = 6
    cost_oranges = 2.70
    num_apples_sell = 5
    num_oranges_sell = 5
    price_apples = 10
    price_oranges = 5
    revenue_apples = (num_apples_sell / 5) * price_apples
    revenue_oranges = num_oranges_sell * price_oranges
    total_revenue = revenue_apples + revenue_oranges
    total_cost = cost_apples + cost_oranges
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())