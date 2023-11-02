def solution():
    
    regular_hours = 40
    regular_rate = 10
    overtime_rate = 15
    overtime_hours = 20
    overtime_pay = overtime_hours * overtime_rate
    regular_pay = regular_hours * regular_rate
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())