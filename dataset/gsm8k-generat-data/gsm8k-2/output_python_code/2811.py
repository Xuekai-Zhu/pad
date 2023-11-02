def solution():
    """A magazine costs $3 each. Jewel bought 10 magazines to be sold at $3.50 each. How much will be Jewel gain from selling these?"""
    cost_per_magazine = 3
    selling_price_per_magazine = 3.5
    total_magazines = 10
    total_cost = cost_per_magazine * total_magazines
    total_revenue = selling_price_per_magazine * total_magazines
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())