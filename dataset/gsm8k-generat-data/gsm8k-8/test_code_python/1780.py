def solution():
    # Define the hourly pay rate, regular hours worked, and overtime hours worked
    hourly_pay_rate = 13.50
    regular_hours = 8 * 5
    overtime_hours = 2 * 5

    # Calculate the regular pay and overtime pay
    regular_pay = hourly_pay_rate * regular_hours
    overtime_pay = hourly_pay_rate * 1.5 * overtime_hours

    # Calculate the total pay for the week
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())