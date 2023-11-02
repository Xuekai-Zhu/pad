def solution():
    hourly_wage = 30  # Hannah makes $30 per hour
    hours_worked = 18  # Hannah works 18 hours per week
    late_deduction = 5  # Hannah's pay is docked $5 each time she's late
    times_late = 3  # Hannah was late 3 times this week

    # Calculate Hannah's total pay before deductions
    total_pay = hourly_wage * hours_worked

    # Calculate Hannah's total deductions for being late
    total_deductions = late_deduction * times_late

    # Calculate Hannah's final pay for the week
    final_pay = total_pay - total_deductions
    result = final_pay
    return result

print(solution())