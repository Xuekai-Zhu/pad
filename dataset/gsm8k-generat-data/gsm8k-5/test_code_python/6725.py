def solution():
    days_worked = 5  # Janice works 5 days a week
    regular_pay = 30  # Janice earns $30 per day
    overtime_pay = 15  # Janice earns an additional $15 for each overtime shift
    overtime_shifts = 3  # Janice works 3 overtime shifts this week

    # Calculate Janice's regular pay for the week
    regular_pay_week = days_worked * regular_pay

    # Calculate Janice's overtime pay for the week
    overtime_pay_week = overtime_shifts * overtime_pay * 2  # Each overtime shift is 2 hours long

    # Calculate Janice's total pay for the week
    total_pay_week = regular_pay_week + overtime_pay_week
    result = total_pay_week
    return result

print(solution())