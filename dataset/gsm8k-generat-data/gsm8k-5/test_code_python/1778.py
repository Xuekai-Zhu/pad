def solution():
    cost_of_ingredients = 53  # Dorothy spent $53 to buy doughnut ingredients
    selling_price_per_doughnut = 3  # Dorothy sells each doughnut for $3
    number_of_doughnuts = 25  # Dorothy made 25 doughnuts

    # Calculate the total revenue from selling the doughnuts
    total_revenue = selling_price_per_doughnut * number_of_doughnuts

    # Calculate Dorothy's profit
    profit = total_revenue - cost_of_ingredients
    result = profit
    return result

print(solution())