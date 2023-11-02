def solution():
    
    regular_rate = 10
    regular_hours = 40
    overtime_rate = regular_rate * 1.2
    regular_pay = regular_hours * regular_rate
    overtime_pay = overtime_rate * overtime_hours
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())