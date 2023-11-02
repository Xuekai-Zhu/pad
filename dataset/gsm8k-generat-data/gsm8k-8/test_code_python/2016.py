def solution():
    # Calculate Vikki's total earnings before deductions
    total_earnings = 42 * 10

    # Calculate the amount deducted for tax
    tax_deduction = 0.2 * total_earnings

    # Calculate the amount deducted for insurance
    insurance_deduction = 0.05 * total_earnings

    # Calculate the total amount deducted
    total_deductions = tax_deduction + insurance_deduction + 5

    # Calculate Vikki's take-home pay
    take_home_pay = total_earnings - total_deductions
    result = take_home_pay
    return result

print(solution())