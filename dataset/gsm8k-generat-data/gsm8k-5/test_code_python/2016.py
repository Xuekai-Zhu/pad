def solution():
    hours_worked = 42  # Vikki worked 42 hours in one week
    hourly_pay_rate = 10  # Vikki's hourly pay rate is $10
    gross_pay = hours_worked * hourly_pay_rate  # Gross pay before deductions

    tax_deduction = 0.2 * gross_pay  # Tax deduction is 20% of gross pay
    insurance_deduction = 0.05 * gross_pay  # Insurance deduction is 5% of gross pay
    union_dues = 5  # $5 is deducted for union dues

    net_pay = gross_pay - tax_deduction - insurance_deduction - union_dues  # Net pay after deductions
    result = net_pay
    return result

print(solution())