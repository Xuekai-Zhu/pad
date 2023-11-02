def solution():
    # Calculate the total amount paid to employees before new hires
    total_pay = 500 * 12 * 10 * 5 * 4  # 500 employees, $12 per hour, 10 hours a day, 5 days a week, 4 weeks a month

    # Calculate the total amount paid to employees after new hires
    total_employees = 500 + 200  # 500 employees before new hires, 200 new hires
    new_total_pay = total_employees * 12 * 10 * 5 * 4  # $12 per hour, 10 hours a day, 5 days a week, 4 weeks a month

    result = new_total_pay
    return result

print(solution())