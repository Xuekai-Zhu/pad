def solution():
    num_cookies = 6 * 12
    sell_price = 1.5
    cost_price = 0.25

    # Calculate the total revenue from selling all cookies
    total_revenue = num_cookies * sell_price

    # Calculate the total cost of making all cookies
    total_cost = num_cookies * cost_price

    # Calculate the total profit
    total_profit = total_revenue - total_cost

    # Calculate the profit for each charity
    charity_profit = total_profit / 2

    result = charity_profit
    return result

print(solution())