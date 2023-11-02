def solution():
    employees = 20
    shirts_per_employee = 20
    hours_per_day = 8
    wage_per_hour = 12
   shirt_bonus = 5
    shirt_price = 35
    daily_expenses = 1000
    total_shirts = employees * shirts_per_employee
    total_revenue = total_shirts * shirt_price
    daily_profit = total_revenue - daily_expenses
    result = daily_profit
    
    return result

print(solution())