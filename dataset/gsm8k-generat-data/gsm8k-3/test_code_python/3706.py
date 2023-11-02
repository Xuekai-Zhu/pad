def solution():
    """Bobby received his weekly paycheck today. Although his salary is $450 per week, his actual paycheck is reduced in size because there are some taxes, insurance payments, and fees removed from his pay before his employer writes the check. If the government removes 1/3 in federal taxes and 8% in state taxes, the health insurance removes $50 per week, the life insurance removes $20 per week, and the city charges him a fee of $10 per week for parking, then what is the final amount left in Bobby's paycheck, in dollars?"""
    # Define the initial salary and the different deductions
    INITIAL_SALARY = 450
    FEDERAL_TAX_RATE = 1/3
    STATE_TAX_RATE = 0.08
    HEALTH_INSURANCE = 50
    LIFE_INSURANCE = 20
    CITY_FEE = 10

    # Calculate the total deductions
    federal_tax = INITIAL_SALARY * FEDERAL_TAX_RATE
    state_tax = INITIAL_SALARY * STATE_TAX_RATE
    total_deductions = federal_tax + state_tax + HEALTH_INSURANCE + LIFE_INSURANCE + CITY_FEE

    # Calculate the final amount left in Bobby's paycheck
    final_amount = INITIAL_SALARY - total_deductions

    # Display the final amount left in Bobby's paycheck
    result = final_amount
    return result

print(solution())