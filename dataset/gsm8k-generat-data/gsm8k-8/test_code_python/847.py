def solution():
    # Calculate the total cost of producing 10 bags of corn
    total_cost = 50 + 35 + 15
    # Calculate the total cost per bag
    cost_per_bag = total_cost / 10
    # Calculate the desired profit per bag
    desired_profit = cost_per_bag * 0.1
    # Calculate the final selling price per bag
    selling_price = cost_per_bag + desired_profit
    result = selling_price
    return result

print(solution())