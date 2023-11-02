def solution():
    # Calculate the total revenue from selling 100 bags at $10 each
    total_revenue = 100 * 10

    # Calculate the total cost of buying 100 bags to make $300 in profit
    total_cost = total_revenue - 300

    # Calculate the cost per bag
    cost_per_bag = total_cost / 100
    result = cost_per_bag
    return result

print(solution())