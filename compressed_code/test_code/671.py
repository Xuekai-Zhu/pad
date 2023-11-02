def solution():
    
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