def solution():
    selling_price = 10  # Each bag is sold for $10
    profit = 300  # Tilly wants to make a profit of $300
    bags_to_sell = 100  # Tilly needs to sell 100 bags

    # Calculate the total revenue from selling the bags
    revenue = selling_price * bags_to_sell

    # Calculate the total cost of purchasing the bags
    cost = revenue - profit

    # Calculate the cost per bag
    cost_per_bag = cost / bags_to_sell
    result = cost_per_bag
    return result

print(solution())