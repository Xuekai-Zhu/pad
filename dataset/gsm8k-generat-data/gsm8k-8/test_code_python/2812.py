def solution():
    # Define the cost and selling price of each magazine
    cost_per_magazine = 3
    selling_price_per_magazine = 3.5

    # Calculate the profit per magazine
    profit_per_magazine = selling_price_per_magazine - cost_per_magazine

    # Calculate the total profit from selling all 10 magazines
    total_profit = profit_per_magazine * 10

    result = total_profit
    return result

print(solution())