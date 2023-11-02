def solution():
    initial_pay = 20
    overtime_pay = initial_pay * 2
    overtime_hours = 10
    total_hours = 40 + overtime_hours
    total_pay = (initial_pay * total_hours) + (overtime_pay * overtime_hours)
    result = total_pay
    return result

print(solution())