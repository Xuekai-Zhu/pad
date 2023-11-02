def solution():
    """Alex gets paid $500 a week and 10% of his weekly income is deducted as tax. He also pays his weekly water bill for $55 and gives away another 10% of his weekly income as a tithe. How much money does Alex have left?"""
    weekly_income = 500
    tax = 0.1 * weekly_income
    water_bill = 55
    tithe = 0.1 * weekly_income
    total_expenses = tax + water_bill + tithe
    remaining_money = weekly_income - total_expenses
    result = remaining_money
    return result

print(solution())