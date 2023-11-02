def solution():
    original_salary = 450
    federal_tax = 1/3
    state_tax = 0.08
    health_insurance = 50
    life_insurance = 20
    parking_fee = 10

    # Calculate the deductions from Bobby's salary
    fed_tax_deduction = original_salary * federal_tax
    state_tax_deduction = original_salary * state_tax
    total_deductions = fed_tax_deduction + state_tax_deduction + \
                        health_insurance + life_insurance + parking_fee

    # Calculate the final amount in Bobby's paycheck
    final_paycheck = original_salary - total_deductions
    result = final_paycheck
    return result

print(solution())