def solution():
    
    opening_cost = 25000
    monthly_revenue = 4000
    monthly_expenses = 1500
    monthly_profit = monthly_revenue - monthly_expenses
    months_to_repay = opening_cost / monthly_profit
    result = months_to_repay
    return result

print(solution())