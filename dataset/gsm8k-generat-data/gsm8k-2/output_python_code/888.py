def solution():
    """Carrie wants to buy a new iPhone. The new iPhone costs $800. She can trade in her Samsung Galaxy for $240. She can make $80 per week babysitting. How many weeks does she have to work before she can purchase the iPhone?"""
    iphone_cost = 800
    trade_in_value = 240
    babysitting_weekly_income = 80
    total_income = trade_in_value
    weeks = 0
    while total_income < iphone_cost:
        weeks += 1
        total_income += babysitting_weekly_income
    result = weeks
    return result

print(solution())