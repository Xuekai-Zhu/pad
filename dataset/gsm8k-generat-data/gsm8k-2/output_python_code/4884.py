def solution():
    """If Jade earns $1600 per month and spent 75% of it on living expenses, one-fifth on insurance, and saves the rest, how much does she save per month?"""
    monthly_income = 1600
    living_expenses = monthly_income * 0.75
    insurance_expenses = monthly_income * 0.2
    savings = monthly_income - living_expenses - insurance_expenses
    result = savings
    return result

print(solution())