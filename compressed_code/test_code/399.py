def solution():
    
    first_center_daily = 10000
    second_center_daily = 3 * first_center_daily
    daily_profit = 0.05 * (first_center_daily + second_center_daily)
    weekly_profit = daily_profit * 7
    result = weekly_profit
    return result

print(solution())