def solution():
    """A magazine costs $3 each. Jewel bought 10 magazines to be sold at $3.50 each. How much will be Jewel gain from selling these?"""
    # Define the cost and selling price of the magazines
    cost_per_magazine = 3
    selling_price_per_magazine = 3.5

    # Calculate the profit per magazine
    profit_per_magazine = selling_price_per_magazine - cost_per_magazine

    # Calculate the total profit from selling 10 magazines
    total_profit = profit_per_magazine * 10

    # return the result
    result = total_profit
    return result

print(solution())