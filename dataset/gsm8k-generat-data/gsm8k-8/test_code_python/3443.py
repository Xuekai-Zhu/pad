def solution():
    # Define Hannah's pay rate and hours worked
    pay_rate = 30
    hours_worked = 18

    # Calculate Hannah's total pay before any deductions
    total_pay = pay_rate * hours_worked

    # Calculate the total amount docked for being late
    total_deductions = 5 * 3

    # Calculate Hannah's final pay after deductions
    final_pay = total_pay - total_deductions
    result = final_pay
    return result

print(solution())