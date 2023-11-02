def solution():
    """Angie is part of a household with shared expenses and contributes $42 a month for necessities. She has a salary of $80 per month. She also pays a share of the household taxes each month. At the end of this month, she had $18 left over. How much did she pay in taxes this month?"""
    necessities_cost = 42
    salary = 80
    remaining_money = 18
    total_expenses = necessities_cost + remaining_money
    taxes = total_expenses - salary
    result = taxes
    return result

print(solution())