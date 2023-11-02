def solution():
    cost_per_bag = 4
    selling_price_per_bag = 8
    num_bags = 30

    # Calculate the total cost of buying all bags of popcorn
    total_cost = cost_per_bag * num_bags

    # Calculate the total revenue from selling all bags of popcorn
    total_revenue = selling_price_per_bag * num_bags

    # Calculate the profit from selling all bags of popcorn
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())