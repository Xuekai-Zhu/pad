def solution():
    # Calculate the cost and revenue for each sale of granola
    cost_per_bag = 3/20  # cost of ingredients for one bag
    revenue_per_bag = 6  # selling price for one bag
    discounted_revenue = 4  # selling price for discounted bags

    # Calculate the total cost and revenue for all bags sold
    total_cost = 3  # cost of ingredients for all bags
    total_revenue = 15 * revenue_per_bag + 5 * discounted_revenue

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())