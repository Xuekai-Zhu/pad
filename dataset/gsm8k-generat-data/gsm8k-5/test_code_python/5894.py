def solution():
    regular_rate = 30  # The regular rate is $30 per hour
    overtime_rate = regular_rate * 1.5  # The overtime rate is 1.5 times the regular rate

    # Calculate the total hours worked for the week
    total_hours_worked = (6 * 3) + (2 * 2 * 40)  # 6 hours per day for the first 3 days, and twice as many hours per day for the remaining 2 days

    # Calculate the total pay for the first 40 hours
    pay_first_40 = regular_rate * 40

    # Calculate the total pay for the overtime hours
    overtime_hours = total_hours_worked - 40
    pay_overtime = overtime_hours * overtime_rate

    # Calculate the total pay for the week
    total_pay = pay_first_40 + pay_overtime
    result = total_pay
    return result

print(solution())