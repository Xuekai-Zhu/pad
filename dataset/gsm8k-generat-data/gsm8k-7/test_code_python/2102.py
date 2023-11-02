def solution():
    monthly_salary = 2000
    tax_percent = 0.2
    insurance_percent = 0.05
    utility_percent = 0.25

    # Calculate the amount deducted for tax and insurance
    deduction_percent = tax_percent + insurance_percent
    total_deduction = deduction_percent * monthly_salary

    # Calculate the amount left after the deductions
    left_after_deductions = monthly_salary - total_deduction

    # Calculate the amount spent on utility bills
    utility_cost = utility_percent * left_after_deductions

    # Calculate the amount left after the utility bills payment
    total_left = left_after_deductions - utility_cost
    result = total_left
    return result

print(solution())