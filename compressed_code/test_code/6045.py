def solution():
    
    daily_income = 40
    tax_rate = 0.1
    net_daily_income = daily_income * (1 - tax_rate)
    days_worked = 30
    total_earned = net_daily_income * days_worked
    result = total_earned
    return result

print(solution())