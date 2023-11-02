def solution():
    """Without factoring in the cost of depreciation for his car John made $30,000 doing Uber. When he finally traded in the car he bought for $18,000 he got $6000 back. What was his profit from driving Uber?"""
    # Define the initial cost of the car and the amount received from trading it in
    initial_cost = 18000
    trade_in_amount = 6000

    # Calculate the profit from Uber
    uber_profit = 30000

    # Subtract the initial cost of the car and add the trade-in amount to get the total profit
    total_profit = uber_profit - initial_cost + trade_in_amount

    result = total_profit
    return result

print(solution())