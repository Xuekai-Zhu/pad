def solution():
    """James buys pistachios for $10 per can. Each can is 5 ounces. He eats 30 ounces of pistachios every 5 days. How much does he spend on pistachios per week?"""
    cost_per_can = 10
    can_size = 5
    daily_consumption = 6 # 30 ounces / 5 days
    weekly_consumption = daily_consumption * 7
    cans_per_week = weekly_consumption / can_size
    total_cost = cans_per_week * cost_per_can
    result = total_cost
    return result

print(solution())