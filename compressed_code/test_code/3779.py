def solution():
    
    monthly_income = 1600
    living_expenses = monthly_income * 0.75
    insurance_expenses = monthly_income * 0.2
    savings = monthly_income - living_expenses - insurance_expenses
    result = savings
    return result

print(solution())