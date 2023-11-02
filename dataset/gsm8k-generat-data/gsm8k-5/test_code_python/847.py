def solution():
    total_cost = 50 + 35 + 15  # The total cost of cultivating the farm
    total_cost_per_bag = total_cost / 10  # The cost per bag of corn

    # Calculate the desired profit per bag of corn
    desired_profit_per_bag = total_cost_per_bag * 0.1

    # Calculate the selling price per bag of corn that will result in the desired profit
    selling_price_per_bag = total_cost_per_bag + desired_profit_per_bag
    result = selling_price_per_bag
    return result

print(solution())