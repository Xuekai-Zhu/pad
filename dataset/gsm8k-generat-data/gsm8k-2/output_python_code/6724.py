def solution():
    """Janice has been working part-time at a convenience store 5 days a week. She can earn $30 per day and can earn $15 more when she works a 2 hour overtime shift. If she works three overtime shifts this week, how much will she earn this week?"""
    days_worked = 5
    base_pay = 30
    overtime_pay = 15
    overtime_shifts = 3
    total_pay = days_worked * base_pay + overtime_shifts * overtime_pay
    result = total_pay
    return result

print(solution())