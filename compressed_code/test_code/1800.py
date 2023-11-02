def solution():
    
    employee_count = 20
    shirts_per_person = 20
    work_hours = 8
    employee_pay_per_hour = 12
    employee_pay_per_shirt = 5
    shirt_price = 35
    non_employee_expenses = 1000
    
    
    employee_expenses_per_day = (employee_count * employee_pay_per_hour * work_hours) + (employee_count * shirts_per_person * employee_pay_per_shirt)
    
    
    total_shirts_per_day = employee_count * shirts_per_person
    revenue_per_day = total_shirts_per_day * shirt_price
    
    
    profits_per_day = revenue_per_day - employee_expenses_per_day - non_employee_expenses
    
    result = profits_per_day
    return result

print(solution())