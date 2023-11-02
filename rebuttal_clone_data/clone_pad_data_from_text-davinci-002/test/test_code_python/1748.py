def solution():
    new_employees = 50
    hours_per_day = 8
    days = 5
    pay_per_hour = 14
    total_hours = new_employees * hours_per_day * days
    total_pay = total_hours * pay_per_hour
    result = total_pay
    return result

print(solution())