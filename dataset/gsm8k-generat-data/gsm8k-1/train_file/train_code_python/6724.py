def solution():
    """Janice has been working part-time at a convenience store 5 days a week. She can earn $30 per day and can earn $15 more when she works a 2 hour overtime shift. If she works three overtime shifts this week, how much will she earn this week?"""
    days_worked = 5
    regular_pay = 30
    overtime_pay = regular_pay + 15
    overtime_shifts = 3
    total_regular_pay = days_worked * regular_pay
    total_overtime_pay = overtime_shifts * overtime_pay
    total_earnings = total_regular_pay + total_overtime_pay
    result = total_earnings
    return result

print(solution())