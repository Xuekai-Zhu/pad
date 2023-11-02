def solution():
    """Angie is part of a household with shared expenses and contributes $42 a month for necessities. She has a salary of $80 per month. She also pays a share of the household taxes each month. At the end of this month, she had $18 left over. How much did she pay in taxes this month?"""
    monthly_expenses = 42
    salary = 80
    leftover_money = 18
    taxes = (salary + leftover_money) - monthly_expenses
    result = taxes
    return result

print(solution())