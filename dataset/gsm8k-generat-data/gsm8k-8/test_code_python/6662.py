def solution():
    base_pay_per_day = 150
    overtime_pay_per_hour = 5
    overtime_hours = 4
    total_days = 5

    base_pay = base_pay_per_day * total_days
    overtime_pay = overtime_pay_per_hour * overtime_hours * total_days
    total_pay = base_pay + overtime_pay
    result = total_pay
    return result

print(solution())