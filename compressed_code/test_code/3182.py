def solution():
    
    regular_hours = 40
    regular_rate = 20
    overtime_hours = 10
    overtime_rate = 40
    total_pay = regular_hours * regular_rate
    total_pay += overtime_hours * overtime_rate
    result = total_pay
    return result

print(solution())