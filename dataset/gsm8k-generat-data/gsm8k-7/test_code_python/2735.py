def solution():
    regular_hourly_rate = 5
    overtime_hourly_rate = 6
    overtime_threshold = 40
    total_hours_week1 = 44
    total_hours_week2 = 48

    # Calculate total pay for week 1
    regular_pay_week1 = regular_hourly_rate * overtime_threshold
    overtime_pay_week1 = (total_hours_week1 - overtime_threshold) * overtime_hourly_rate
    total_pay_week1 = regular_pay_week1 + overtime_pay_week1

    # Calculate total pay for week 2
    regular_pay_week2 = regular_hourly_rate * overtime_threshold
    overtime_pay_week2 = (total_hours_week2 - overtime_threshold) * overtime_hourly_rate
    total_pay_week2 = regular_pay_week2 + overtime_pay_week2

    # Calculate total pay for both weeks
    total_pay = total_pay_week1 + total_pay_week2
    result = total_pay
    return result

print(solution())