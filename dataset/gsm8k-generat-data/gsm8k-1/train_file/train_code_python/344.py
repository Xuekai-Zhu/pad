def solution():
    """Adam earns $40 daily in his job. 10% of his money is deducted as taxes. How much money will Adam have earned after taxes after 30 days of work?"""
    daily_income = 40
    tax_rate = 0.1
    net_daily_income = daily_income * (1 - tax_rate)
    days_worked = 30
    total_earned = net_daily_income * days_worked
    result = total_earned
    return result

print(solution())