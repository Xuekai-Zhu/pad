def solution():
    hours_worked = 42
    hourly_rate = 10

    # Calculate Vikki's gross pay for the week
    gross_pay = hours_worked * hourly_rate

    # Calculate the total deductions
    tax_deduction = 0.20 * gross_pay
    insurance_deduction = 0.05 * gross_pay
    union_dues = 5

    total_deductions = tax_deduction + insurance_deduction + union_dues

    # Calculate Vikki's net take-home pay
    net_pay = gross_pay - total_deductions
    result = net_pay
    return result

print(solution())