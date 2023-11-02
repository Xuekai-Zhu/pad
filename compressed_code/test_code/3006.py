def solution():
    
    work_days = 10 
    paid_vacation_days = 6
    unpaid_vacation_days = work_days - paid_vacation_days
    daily_pay = 15 * 8 
    total_unpaid_pay = daily_pay * unpaid_vacation_days
    result = total_unpaid_pay
    return result

print(solution())