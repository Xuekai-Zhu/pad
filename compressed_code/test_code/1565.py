def solution():
    
    hours_worked = 42
    hourly_pay_rate = 10
    weekly_earnings = hours_worked * hourly_pay_rate
    tax_deduction = 0.2 * weekly_earnings
    insurance_deduction = 0.05 * weekly_earnings
    union_dues = 5
    total_deductions = tax_deduction + insurance_deduction + union_dues
    take_home_pay = weekly_earnings - total_deductions
    result = take_home_pay
    return result

print(solution())