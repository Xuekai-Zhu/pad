def solution():
    
    regular_rate = 10
    overtime_rate = regular_rate * 1.2
    regular_hours = 40
    overtime_hours = 45 - regular_hours
    regular_pay = regular_hours * regular_rate
    overtime_pay = overtime_hours * overtime_rate
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())