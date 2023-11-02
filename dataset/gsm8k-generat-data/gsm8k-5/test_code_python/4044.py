def solution():
    hourly_rate_regular = 10  # Janice gets paid $10 an hour for the first 40 hours she works
    hourly_rate_overtime = 15  # Janice gets paid $15 per hour for overtime work
    regular_hours_worked = 40  # Janice works 40 regular hours per week
    overtime_hours_worked = 20  # Janice works 20 overtime hours in the week

    # Calculate Janice's regular pay
    regular_pay = hourly_rate_regular * regular_hours_worked

    # Calculate Janice's overtime pay
    overtime_pay = hourly_rate_overtime * overtime_hours_worked

    # Calculate Janice's total pay for the week
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())