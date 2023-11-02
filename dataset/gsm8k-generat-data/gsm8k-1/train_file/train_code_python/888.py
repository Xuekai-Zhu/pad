def solution():
    """Carrie wants to buy a new iPhone. The new iPhone costs $800. She can trade in her Samsung Galaxy for $240. She can make $80 per week babysitting. How many weeks does she have to work before she can purchase the iPhone?"""
    iphone_cost = 800
    trade_in_value = 240
    weekly_income = 80
    weeks_to_save = (iphone_cost - trade_in_value) / weekly_income
    result = weeks_to_save
    return result

print(solution())