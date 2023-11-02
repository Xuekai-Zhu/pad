def solution():
    
    days_worked = 5
    base_pay = 30
    overtime_pay = 15
    overtime_shifts = 3
    total_pay = days_worked * base_pay + overtime_shifts * overtime_pay
    result = total_pay
    return result

print(solution())