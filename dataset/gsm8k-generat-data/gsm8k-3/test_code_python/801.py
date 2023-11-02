def solution():
    """Alex gets paid $500 a week and 10% of his weekly income is deducted as tax. He also pays his weekly water bill for $55 and gives away another 10% of his weekly income as a tithe. How much money does Alex have left?"""
    # Define Alex's weekly salary and the tax and tithe rates
    WEEKLY_SALARY = 500
    TAX_RATE = 0.1
    TITHE_RATE = 0.1

    # Calculate Alex's deductions for tax and tithe
    tax_deduction = WEEKLY_SALARY * TAX_RATE
    tithe_deduction = WEEKLY_SALARY * TITHE_RATE

    # Calculate Alex's remaining income after deductions
    remaining_income = WEEKLY_SALARY - tax_deduction - 55 - tithe_deduction

    # Display Alex's remaining income
    result = remaining_income
    return result

print(solution())