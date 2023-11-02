def solution():
    """Without factoring in the cost of depreciation for his car John made $30,000 doing Uber. When he finally traded in the car he bought for $18,000 he got $6000 back. What was his profit from driving Uber?"""
    earnings = 30000
    initial_cost = 18000
    resale_value = 6000
    total_cost = initial_cost - resale_value
    profit = earnings - total_cost
    result = profit
    return result

print(solution())