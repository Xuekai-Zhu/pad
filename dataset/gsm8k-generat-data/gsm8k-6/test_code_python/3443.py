def solution():
    # Calculate Hannah's total pay before deductions
    total_pay = 30 * 18  # Hannah makes $30/hour and works 18 hours per week

    # Calculate the total deductions for being late
    total_deductions = 5 * 3  # Hannah is docked $5 each time she's late and was late 3 times

    # Calculate Hannah's final pay after deductions
    final_pay = total_pay - total_deductions
    result = final_pay
    return result

print(solution())