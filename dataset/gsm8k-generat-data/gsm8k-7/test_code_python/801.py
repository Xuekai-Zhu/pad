def solution():
    weekly_income = 500
    tax_percentage = 0.1
    water_bill = 55
    tithe_percentage = 0.1

    # Calculate the amount of tax deducted from Alex's income
    tax_amount = weekly_income * tax_percentage

    # Calculate the amount of money Alex gives as his tithe
    tithe_amount = weekly_income * tithe_percentage

    # Calculate the total amount of money deducted from Alex's income
    total_deductions = tax_amount + water_bill + tithe_amount

    # Calculate the amount of money Alex has left after deductions
    money_left = weekly_income - total_deductions
    result = money_left
    return result

print(solution())