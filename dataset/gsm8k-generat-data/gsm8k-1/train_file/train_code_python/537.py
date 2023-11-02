def solution():
    """A luxury bag costs $3000. A reseller wants to get a 15% profit. How much should she sell the bag?"""
    cost_price = 3000
    profit_percent = 15
    selling_price = cost_price * ((100 + profit_percent) / 100)
    result = selling_price
    return result

print(solution())