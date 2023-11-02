def solution():
    # Calculate total deductions
    tax_deduction = 0.20 * 40000
    healthcare_deduction = 0.10 * 40000
    union_dues = 800
    total_deductions = tax_deduction + healthcare_deduction + union_dues

    # Calculate take-home pay
    take_home_pay = 40000 - total_deductions
    result = take_home_pay
    return result

print(solution())