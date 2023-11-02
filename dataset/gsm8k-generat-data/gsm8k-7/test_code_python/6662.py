def solution():
    daily_pay = 150
    overtime_pay = 5
    overtime_hours = 4
    num_days = 5

    # Calculate the total regular pay for 5 days
    regular_pay = daily_pay * num_days

    # Calculate the total overtime pay for 4 hours each day for 5 days
    overtime_total = overtime_pay * overtime_hours * num_days

    # Calculate the total pay for 5 days with overtime
    total_pay = regular_pay + overtime_total
    result = total_pay
    return result

print(solution())