def solution():
    # Calculate the cost per orange
    cost_per_orange = 12.50 / 25

    # Calculate the selling price per orange
    selling_price_per_orange = 0.60

    # Calculate the profit per orange in cents
    profit_per_orange = (selling_price_per_orange - cost_per_orange) * 100
    result = profit_per_orange
    return result

print(solution())