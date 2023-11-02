def solution():
    # Calculate the total number of hours worked in the week
    total_hours = (6 * 3) + (2 * 2 * (24 / 5))  # 6 hours for the first three days and twice the hours for the remaining two days (assuming 5-day workweek)

    # Calculate the total pay for the first 40 hours worked
    regular_pay = 30 * min(total_hours, 40)

    # Calculate the pay for the additional hours worked (after 40 hours)
    overtime_pay = 0
    if total_hours > 40:
        overtime_hours = total_hours - 40
        overtime_pay = 30 * 1.5 * overtime_hours

    # Calculate the total pay for the week
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())