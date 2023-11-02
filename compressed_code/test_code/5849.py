def solution():
    
    base_pay = 500
    regular_hours = 40
    overtime_rate = 20
    overtime_hours = 10
    total_pay = base_pay + ((overtime_rate * overtime_hours))
    result = total_pay
    return result

print(solution())