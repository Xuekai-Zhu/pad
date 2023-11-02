def solution():
    
    hourly_rate = 20
    overtime_rate = 1.5 * hourly_rate
    regular_hours = 40
    overtime_hours = 52 - regular_hours
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * overtime_rate
    total_pay = regular_pay + overtime_pay
    weeks_to_purchase = 4640 / total_pay
    result = weeks_to_purchase
    return result

print(solution())