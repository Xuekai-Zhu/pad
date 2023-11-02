def solution():
    # Define the cost and selling price of one pot of lily of the valley
    cost_per_pot = 12
    selling_price_per_pot = cost_per_pot * 1.25

    # Calculate the total revenue from selling 150 pots
    total_revenue = selling_price_per_pot * 150

    # Calculate the profit made by Françoise
    profit = total_revenue - (cost_per_pot * 150)

    result = profit
    return result

print(solution())