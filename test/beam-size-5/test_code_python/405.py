def solution():
    num_employees = 40
    hourly_rate = 15
    num_hours_worked = 40
    num_expired_employees = num_employees / 4

    # Calculate the total amount paid to employees in May
    total_employee_pay = num_employees * hourly_rate * num_hours_worked

    # Calculate the total amount paid to employees in June
    total_june_pay = num_expired_employees * hourly_rate * num_hours_worked

    # Calculate the total amount paid to employees in June
    total_payment = total_employee_pay + total_june_pay
    result = total_payment
    return result

print(solution())