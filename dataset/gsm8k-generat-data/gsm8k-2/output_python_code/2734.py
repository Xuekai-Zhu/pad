def solution():
    """Bob gets paid $5 an hour for the regular hours he works
    and $6 an hour for any overtime hours he works. All hours over 40 in a week
    are considered overtime. If Bob works 44 hours in the first week and 48 hours in
    the second week, how much did he make?"""
    regular_pay_rate = 5
    overtime_pay_rate = 6
    first_week_hours = 44
    second_week_hours = 48
    if first_week_hours <= 40:
        first_week_pay = first_week_hours * regular_pay_rate
    else:
        first_week_pay = 40 * regular_pay_rate + (first_week_hours - 40) * overtime_pay_rate
    if second_week_hours <= 40:
        second_week_pay = second_week_hours * regular_pay_rate
    else:
        second_week_pay = 40 * regular_pay_rate + (second_week_hours - 40) * overtime_pay_rate
    total_pay = first_week_pay + second_week_pay
    result = total_pay
    return result

print(solution())