def solution():
    rent_per_week = 20
    earnings_per_day = 8
    days_per_week = 7

    # Calculate Alton's total earnings per week
    total_earnings = earnings_per_day * days_per_week

    # Calculate Alton's weekly profit (earnings minus rent)
    weekly_profit = total_earnings - rent_per_week
    result = weekly_profit
    return result

print(solution())