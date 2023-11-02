def solution():
    basic_salary = 1250
    commission = 0.10
    sales = 23600
    total_earnings = basic_salary + (commission * sales)
    savings = total_earnings * 0.20
    monthly_expenses = total_earnings - savings
    result = monthly_expenses
    return result

print(solution())