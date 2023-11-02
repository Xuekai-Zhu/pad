def solution():
    
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