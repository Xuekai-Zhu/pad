def solution():
    
    cash_register_cost = 1040
    daily_sales = (40 * 2) + (6 * 12)
    daily_expenses = 20 + 2
    daily_profit = daily_sales - daily_expenses
    days_to_pay_off = cash_register_cost / daily_profit
    result = days_to_pay_off
    return result

print(solution())