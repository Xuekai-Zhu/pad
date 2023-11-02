def solution():
    """Without factoring in the cost of depreciation for his car John made $30,000 doing Uber. When he finally traded in the car he bought for $18,000 he got $6000 back. What was his profit from driving Uber?"""
    earnings = 30000
    car_cost = 18000
    trade_in_value = 6000
    profit = earnings - (car_cost - trade_in_value)
    result = profit
    return result

print(solution())