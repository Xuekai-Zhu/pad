def solution():
    # Calculate Bob's pay for the first and second week of work
    regular_pay_week1 = 5 * 40  # Bob works 40 regular hours at $5/hour in the first week
    overtime_pay_week1 = 6 * 4  # Bob works 4 overtime hours at $6/hour in the first week
    total_pay_week1 = regular_pay_week1 + overtime_pay_week1  # Bob's total pay for the first week
    regular_pay_week2 = 5 * 40  # Bob works 40 regular hours at $5/hour in the second week
    overtime_pay_week2 = 6 * 8  # Bob works 8 overtime hours at $6/hour in the second week
    total_pay_week2 = regular_pay_week2 + overtime_pay_week2  # Bob's total pay for the second week

    # Calculate Bob's total pay for both weeks combined
    total_pay = total_pay_week1 + total_pay_week2
    result = total_pay
    return result

print(solution())