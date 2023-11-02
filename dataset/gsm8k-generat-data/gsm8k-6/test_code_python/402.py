def solution():
    # Calculate the total revenue of the movie
    total_revenue = 3.5 * 120  # movie makes 3.5 times the opening weekend revenue

    # Calculate the production costs and subtract it from the revenue
    production_cost = 60
    net_profit = 0.6 * (total_revenue - production_cost)  # production company keeps 60% of the profit

    result = net_profit
    return result

print(solution())