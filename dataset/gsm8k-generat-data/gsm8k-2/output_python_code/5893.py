def solution():
    """An employee makes 30 dollars an hour for the first 40 hours in the workweek and an additional 50% for every hour above 40 in the week. If he works 6 hours for the first 3 days in the workweek and twice as many hours per day for the remaining 2 days, how much money did he make?"""
    regular_pay_rate = 30
    overtime_pay_rate = regular_pay_rate * 1.5
    total_hours = 6 * 3 + 2 * 6 * 2
    if total_hours <= 40:
        pay = total_hours * regular_pay_rate
    else:
        regular_hours = 40
        overtime_hours = total_hours - regular_hours
        pay = regular_hours * regular_pay_rate + overtime_hours * overtime_pay_rate

    result = pay
    return result

print(solution())