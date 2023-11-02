def solution():
    regular_pay_rate = 10
    overtime_pay_rate = 15
    regular_hours = 40
    total_hours = 60
    
    # Calculate the total regular pay
    regular_pay = regular_hours * regular_pay_rate
    
    # Calculate the total overtime hours
    overtime_hours = total_hours - regular_hours
    
    # Calculate the total overtime pay
    overtime_pay = overtime_hours * overtime_pay_rate
    
    # Calculate the total pay
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())