def solution():
    
    hours_worked = 42
    hourly_pay_rate = 10
    earnings = hours_worked * hourly_pay_rate
    tax = 0.2 * earnings
    insurance = 0.05 * earnings
    union_dues = 5
    total_deductions = tax + insurance + union_dues
    take_home_pay = earnings - total_deductions
    result = take_home_pay
    return result

print(solution())