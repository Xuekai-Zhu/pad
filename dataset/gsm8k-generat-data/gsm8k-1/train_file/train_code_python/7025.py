def solution():
    """Alton owns a business. He is currently renting a space that costs $20 per week. If Alton earns $8 per day, how much is his total profit every week?"""
    rent_per_week = 20
    earning_per_day = 8
    days_per_week = 7
    total_earning = earning_per_day * days_per_week
    total_profit = total_earning - rent_per_week
    result = total_profit
    return result

print(solution())