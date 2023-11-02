def solution():
    mining_profit = 3000000
    oil_profit = 5000000
    monthly_expenses = 30000000
    annual_profits = (mining_profit + oil_profit) * 12 - monthly_expenses
    fine_amount = annual_profits * 0.01
    result = fine_amount
    
    return result

print(solution())