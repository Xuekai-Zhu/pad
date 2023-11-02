def solution():
    """Gary manages two Amazon distribution centers. The first center processes 10000 packages per day, and the second center processes three times that volume. If Amazon makes 5 cents of profit per package, how much profit per week do the two centers make combined?"""
    first_center_daily = 10000
    second_center_daily = 3 * first_center_daily
    daily_profit = 0.05 * (first_center_daily + second_center_daily)
    weekly_profit = daily_profit * 7
    result = weekly_profit
    return result

print(solution())