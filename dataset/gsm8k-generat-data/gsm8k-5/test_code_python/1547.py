def solution():
    cost_per_bag = 4  # John buys each bag of popcorn for $4
    selling_price_per_bag = 8  # John sells each bag of popcorn for $8
    number_of_bags = 30  # John sells 30 bags of popcorn

    # Calculate the total cost of buying 30 bags of popcorn
    total_cost = cost_per_bag * number_of_bags

    # Calculate the total revenue from selling 30 bags of popcorn
    total_revenue = selling_price_per_bag * number_of_bags

    # Calculate the profit John makes from selling 30 bags of popcorn
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())