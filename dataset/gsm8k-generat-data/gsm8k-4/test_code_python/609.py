def solution():
    """Angie is part of a household with shared expenses and contributes $42 a month for necessities. She has a salary of $80 per month. She also pays a share of the household taxes each month. At the end of this month, she had $18 left over. How much did she pay in taxes this month?"""
    # Define Angie's monthly contributions
    necessities_contribution = 42
    salary = 80

    # Calculate Angie's total income
    total_income = necessities_contribution + salary + 18

    # Calculate Angie's taxes for the month
    taxes = total_income - necessities_contribution - salary

    result = taxes
    return result

print(solution())