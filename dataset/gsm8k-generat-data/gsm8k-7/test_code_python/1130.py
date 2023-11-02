def solution():
    max_daily_deliveries = 35
    max_daily_unloads = max_daily_deliveries / 7

    # Max delivered the maximum number of packages twice
    deliveries = max_daily_deliveries * 2

    # Max unloaded a total of 50 packages on two other days
    unloads = 50

    # Max unloaded one-seventh of the maximum possible daily performance on one day
    unloads += max_daily_unloads / 7

    # The sum of the packages transported on the last two days was only fourth-fifth of the maximum daily performance
    deliveries += max_daily_deliveries * 4/5 * 2

    max_weekly_deliveries = max_daily_deliveries * 7
    diff = max_weekly_deliveries - (deliveries + unloads)
    return diff

print(solution())