def solution():
     monthly_earnings = 18 * 80
     monthly_expenses = 280 + (monthly_earnings * 0.2)
     monthly_savings = monthly_earnings - monthly_expenses
     result = monthly_savings
     return result

print(solution())