def solution():
    # Calculate the cost of each orange and the profit made on each orange
    cost_per_orange = 12.5 / 25  # $12.50 for 25 oranges
    selling_price_per_orange = 0.6
    profit_per_orange = round((selling_price_per_orange - cost_per_orange) * 100)  # round to nearest cent

    result = profit_per_orange
    return result

print(solution())