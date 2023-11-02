def solution():
    """Without factoring in the cost of depreciation for his car John made $30,000 doing Uber.  When he finally traded in the car he bought for $18,000 he got $6000 back.  What was his profit from driving Uber?"""
    # Define the amount John made from Uber and the cost of his car
    UBER_INCOME = 30000
    CAR_COST = 18000

    # Calculate John's profit
    profit = UBER_INCOME - (CAR_COST - 6000)

    # Display John's profit
    result = profit
    return result

print(solution())