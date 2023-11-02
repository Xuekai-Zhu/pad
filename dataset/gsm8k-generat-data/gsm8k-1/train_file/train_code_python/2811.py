def solution():
    """A magazine costs $3 each. Jewel bought 10 magazines to be sold at $3.50 each. How much will be Jewel gain from selling these?"""
    cost_per_magazine = 3
    selling_price_per_magazine = 3.5
    magazines_bought = 10
    profit_per_magazine = selling_price_per_magazine - cost_per_magazine
    total_profit = profit_per_magazine * magazines_bought
    result = total_profit
    return result

print(solution())