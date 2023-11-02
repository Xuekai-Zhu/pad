def solution():
    hourly_wage = 18.0
    regular_hours_per_day = 8
    overtime_hours_per_day = 2
    overtime_rate = 1.5

    # Calculate the total regular hours worked in a week
    total_regular_hours = regular_hours_per_day * 5

    # Calculate the total overtime hours worked in a week
    total_overtime_hours = overtime_hours_per_day * 5

    # Calculate the total regular pay
    regular_pay = hourly_wage * total_regular_hours

    # Calculate the total overtime pay
    overtime_pay = (hourly_wage * overtime_rate) * total_overtime_hours

    # Calculate the total pay
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())