def solution():
    # Calculate the total cost of making the granola
    total_cost = 3 * 20

    # Calculate the revenue earned from selling the 15 bags at the regular price
    regular_price_revenue = 15 * 6

    # Calculate the revenue earned from selling the remaining 5 bags at the discounted price
    discounted_price_revenue = 5 * 4

    # Calculate the total revenue earned
    total_revenue = regular_price_revenue + discounted_price_revenue

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())