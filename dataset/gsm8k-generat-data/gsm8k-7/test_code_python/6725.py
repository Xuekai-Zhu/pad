def solution():
    days_worked = 5
    daily_pay = 30
    overtime_pay = 15
    num_overtime_shifts = 3
    overtime_hours = 2

    # Calculate the total pay for regular work days
    regular_pay = days_worked * daily_pay

    # Calculate the total pay for overtime shifts
    overtime_pay_total = num_overtime_shifts * overtime_pay * overtime_hours

    # Calculate the total pay for the week
    total_pay = regular_pay + overtime_pay_total
    result = total_pay
    return result

print(solution())