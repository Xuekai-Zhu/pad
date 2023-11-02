def solution():
    regular_pay = 10
    overtime_pay = 15
    regular_hours = 40
    overtime_hours = 20
    total_pay = (regular_hours * regular_pay) + (overtime_hours * overtime_pay)
    result = total_pay
    return result

print(solution())