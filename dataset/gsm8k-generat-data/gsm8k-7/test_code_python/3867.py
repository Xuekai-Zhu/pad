def solution():
    num_workdays = 10  # 2 weeks x 5 workdays per week - 6 paid vacation days
    unpaid_vacation_days = 4  # 2 weeks x 2 weekend days per week
    pay_per_hour = 15
    hours_per_day = 8

    # Calculate the total number of work hours Susan would have worked
    total_work_hours = num_workdays * hours_per_day

    # Calculate the number of unpaid vacation hours Susan will take
    unpaid_vacation_hours = unpaid_vacation_days * hours_per_day

    # Calculate the total number of paid vacation hours Susan will take
    paid_vacation_hours = 6 * hours_per_day

    # Calculate the total pay Susan will miss on her vacation
    missed_pay = (total_work_hours - paid_vacation_hours - unpaid_vacation_hours) * pay_per_hour

    result = missed_pay
    return result

print(solution())