def solution():
    num_bags = 100
    selling_price_per_bag = 10
    total_profit = 300

    # Calculate the total revenue from selling 100 bags at $10 per bag
    total_revenue = num_bags * selling_price_per_bag

    # Calculate the total cost of all the bags that Tilly bought
    total_cost = total_revenue - total_profit

    # Calculate the cost per bag that Tilly bought
    cost_per_bag = total_cost / num_bags
    result = cost_per_bag
    return result

print(solution())