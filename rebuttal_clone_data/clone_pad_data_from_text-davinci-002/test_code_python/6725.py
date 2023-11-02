def solution():
    regular_hours = 5 * 30
    overtime_hours = 3 * 2
    hourly_rate = 30
    overtime_rate = hourly_rate + 15
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * overtime_rate
    total_pay = regular_pay + overtime_pay
    result = total_pay
    
    return result

print(solution())