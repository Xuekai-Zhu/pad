def solution():
    base_pay_rate = 20
    overtime_pay_rate = base_pay_rate * 2
    max_hours = 40
    weekly_hours = 50

    # Calculate the total pay for the first 40 hours
    base_pay = min(max_hours, weekly_hours) * base_pay_rate

    # Calculate the total pay for any overtime hours
    overtime_hours = max(weekly_hours - max_hours, 0)
    overtime_pay = overtime_hours * overtime_pay_rate

    # Calculate the total pay for the entire workweek
    total_pay = base_pay + overtime_pay
    result = total_pay
    return result

print(solution())