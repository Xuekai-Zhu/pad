def solution():
    
    iphone_cost = 800
    trade_in_value = 240
    weekly_income = 80
    weeks_to_save = (iphone_cost - trade_in_value) / weekly_income
    result = weeks_to_save
    return result

print(solution())