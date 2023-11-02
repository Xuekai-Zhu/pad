def solution():
    # Define the cost and selling price of each sweater
    cost_per_sweater = 4 * 6
    selling_price_per_sweater = 35

    # Calculate Chantal's profit per sweater
    profit_per_sweater = selling_price_per_sweater - cost_per_sweater

    # Calculate Chantal's total profit for 28 sweaters
    total_profit = 28 * profit_per_sweater
    result = total_profit
    return result

print(solution())