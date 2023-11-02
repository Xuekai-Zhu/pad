def solution():
    cost_per_rug = 40  # Mrs. Oaklyn buys each rug at $40
    selling_price_per_rug = 60  # Mrs. Oaklyn sells each rug at $60
    number_of_rugs = 20  # Mrs. Oaklyn buys 20 rugs

    # Calculate the total cost of the rugs
    total_cost = cost_per_rug * number_of_rugs

    # Calculate the total revenue from selling the rugs
    total_revenue = selling_price_per_rug * number_of_rugs

    # Calculate the profit from selling the rugs
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())