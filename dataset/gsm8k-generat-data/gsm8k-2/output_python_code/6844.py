def solution():
    """A vendor bought apples at 2 for $3 and plans to sell them at 5 for $10. He also bought 3 oranges for $2.70 and plans to sell them at $1 each. How much is his profit if he sells 5 apples and 5 oranges?"""
    apples_total_cost = (5/2) * 3  # cost of 5 apples
    apples_total_revenue = (5/5) * 10  # revenue from selling 5 apples
    oranges_total_cost = 2.70
    oranges_total_revenue = 5  # revenue from selling 5 oranges
    total_profit = (apples_total_revenue + oranges_total_revenue) - (apples_total_cost + oranges_total_cost)
    result = total_profit
    return result

print(solution())