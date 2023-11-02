def solution():
    """Angie is part of a household with shared expenses and contributes $42 a month for necessities. She has a salary of $80 per month. She also pays a share of the household taxes each month. At the end of this month, she had $18 left over. How much did she pay in taxes this month?"""
    # Define Angie's monthly expenses
    necessities = 42
    salary = 80
    total_expenses = necessities + salary

    # Calculate the amount Angie paid in taxes
    taxes = total_expenses - 18 - necessities - salary

    # Display the amount of taxes Angie paid
    result = taxes
    return result

print(solution())