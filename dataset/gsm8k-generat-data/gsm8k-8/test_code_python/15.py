def solution():
    # Calculate the cost and revenue per DVD
    dvd_cost = 2000 + 6
    dvd_revenue = 2.5 * dvd_cost

    # Calculate the profit per DVD
    dvd_profit = dvd_revenue - dvd_cost

    # Calculate the total profit per week and for 20 weeks
    weekly_profit = dvd_profit * 500 * 5
    total_profit = weekly_profit * 20
    result = total_profit
    return result

print(solution())