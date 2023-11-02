def solution():
    """Elizabeth uses $3.00 worth of ingredients to make a bag of granola. She makes 20 bags and sells them for $6.00 a bag at the farmer's market. An hour before closing, she has sold 15 bags and marks the remaining 5 bags down to $4.00 and sells them soon after. What is her net profit?"""
    cost_per_bag = 3
    selling_price_full_price = 6
    selling_price_marked_down = 4
    num_bags = 20
    num_bags_sold_full_price = 15
    num_bags_sold_marked_down = 5

    revenue_full_price = selling_price_full_price * num_bags_sold_full_price
    revenue_marked_down = selling_price_marked_down * num_bags_sold_marked_down

    total_revenue = revenue_full_price + revenue_marked_down
    total_cost = cost_per_bag * num_bags

    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())