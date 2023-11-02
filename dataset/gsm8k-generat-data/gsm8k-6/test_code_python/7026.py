def solution():
    # Calculate Alton's weekly profit
    daily_profit = 8  # Alton earns $8 per day
    weekly_rent = 20  # Alton pays $20 per week for rent
    weekly_profit = (daily_profit * 7) - weekly_rent  # Alton works 7 days a week, subtracting the rent from total earnings 
    result = weekly_profit
    return result

print(solution())