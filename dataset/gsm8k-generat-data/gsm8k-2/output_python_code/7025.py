def solution():
    """Alton owns a business. He is currently renting a space that costs $20 per week. If Alton earns $8 per day, how much is his total profit every week?"""
    rent_cost = 20
    daily_income = 8
    weekly_profit = (daily_income * 7) - rent_cost
    result = weekly_profit
    return result

print(solution())