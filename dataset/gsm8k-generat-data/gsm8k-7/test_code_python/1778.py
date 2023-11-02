def solution():
    cost_of_ingredients = 53
    num_doughnuts = 25
    price_per_doughnut = 3

    # Calculate the total revenue from selling all 25 doughnuts
    total_revenue = num_doughnuts * price_per_doughnut

    # Calculate the profit by subtracting the cost of ingredients from the total revenue
    profit = total_revenue - cost_of_ingredients
    result = profit
    return result

print(solution())