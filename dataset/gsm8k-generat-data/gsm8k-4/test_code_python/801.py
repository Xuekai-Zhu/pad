def solution():
    """Alex gets paid $500 a week and 10% of his weekly income is deducted as tax. He also pays his weekly water bill for $55 and gives away another 10% of his weekly income as a tithe. How much money does Alex have left?"""
    # Define Alex's weekly income and the percentage of income deducted as tax and tithe
    WEEKLY_INCOME = 500
    TAX_PERCENTAGE = 0.1
    TITHE_PERCENTAGE = 0.1
    WATER_BILL = 55

    # Calculate the amount of tax deducted from Alex's income
    tax = WEEKLY_INCOME * TAX_PERCENTAGE

    # Calculate the amount of money Alex gives away as a tithe
    tithe = WEEKLY_INCOME * TITHE_PERCENTAGE

    # Calculate the amount of money Alex has left after tax, tithe, and water bill
    left_over = WEEKLY_INCOME - tax - tithe - WATER_BILL

    # Return the amount of money Alex has left
    result = left_over
    return result

print(solution())