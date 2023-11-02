def solution():
    cost_per_bag = 3.00  # Elizabeth uses $3.00 worth of ingredients to make one bag of granola
    selling_price_normal = 6.00  # Elizabeth sells one bag of granola for $6.00
    selling_price_marked_down = 4.00  # Elizabeth sells marked down bags for $4.00
    num_bags_normal = 15  # Elizabeth sells 15 bags at the normal price
    num_bags_marked_down = 5  # Elizabeth marks down and sells 5 bags

    # Calculate Elizabeth's revenue from selling 15 bags at the normal price
    revenue_normal = num_bags_normal * selling_price_normal

    # Calculate Elizabeth's revenue from selling 5 bags at the marked down price
    revenue_marked_down = num_bags_marked_down * selling_price_marked_down

    # Calculate Elizabeth's total revenue
    total_revenue = revenue_normal + revenue_marked_down

    # Calculate Elizabeth's total cost
    total_cost = cost_per_bag * 20  # Elizabeth makes 20 bags in total

    # Calculate Elizabeth's net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())