def solution():
    hourly_wage = 30
    hours_worked = 18
    late_fee = 5
    num_late = 3

    # Calculate the total pay before any deductions
    pay_before_deductions = hourly_wage * hours_worked

    # Calculate the total amount of late fees deducted from pay
    total_late_fees = num_late * late_fee

    # Calculate the final pay after all deductions
    final_pay = pay_before_deductions - total_late_fees

    result = final_pay
    return result

print(solution())