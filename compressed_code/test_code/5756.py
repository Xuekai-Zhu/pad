def solution():
    
    income = 65000
    expenses = 20000 + 5000 + 8000
    savings_goal = 42000
    additional_income_needed = (expenses + savings_goal) - income
    result = additional_income_needed
    return result

print(solution())