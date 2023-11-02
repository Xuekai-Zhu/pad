def solution():
    """James buys pistachios for $10 per can. Each can is 5 ounces. He eats 30 ounces of pistachios every 5 days. How much does he spend on pistachios per week?"""
    cost_per_can = 10
    ounces_per_can = 5
    ounces_per_week = 30
    cans_per_week = ounces_per_week / ounces_per_can
    cost_per_week = cans_per_week * cost_per_can
    result = cost_per_week
    return result

print(solution())