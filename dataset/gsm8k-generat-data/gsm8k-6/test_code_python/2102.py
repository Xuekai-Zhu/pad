def solution():
    # Calculate Maria's deductions
    tax = 0.2 * 2000  # 20% of the salary goes to tax
    insurance = 0.05 * 2000  # 5% of the salary goes to insurance
    total_deductions = tax + insurance  # total amount of deductions

    # Calculate the money left after deductions
    money_left = 2000 - total_deductions

    # Calculate the amount spent on utility bills
    utility_bills = 0.25 * money_left

    # Calculate the final amount of money Maria has
    final_money = money_left - utility_bills

    result = final_money
    return result

print(solution())