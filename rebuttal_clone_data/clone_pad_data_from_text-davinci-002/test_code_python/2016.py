def solution():
    hours_worked = 42
    hourly_rate = 10
    weekly_earnings = hours_worked * hourly_rate
    tax_rate = 20
    tax_amount = weekly_earnings * (tax_rate / 100)
    insurance_amount = weekly_earnings * (5 / 100)
    dues = 5
    total_deductions = tax_amount + insurance_amount + dues
    net_pay = weekly_earnings - total_deductions
    result = net_pay
    
    return result

print(solution())