def solution():
    hourly_rate = 18.00
    regular_hours_per_day = 8
    overtime_rate = hourly_rate * 1.5  # The overtime rate is hourly rate + 1/2 hourly rate
    overtime_hours_per_day = 2  # Tina works 10 hours per day, 2 of which are overtime hours
    days_per_week = 5

    # Calculate the total pay for regular hours
    regular_pay = hourly_rate * regular_hours_per_day * days_per_week

    # Calculate the total pay for overtime hours
    overtime_pay = overtime_rate * overtime_hours_per_day * days_per_week

    # Calculate the total pay for the week
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())