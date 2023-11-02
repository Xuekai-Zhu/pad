def solution():
    """Faith is getting paid $13.50 per hour. She normally works 8 hours a day, 5 days a week, plus 2 hours of overtime per day. How much will she earn by the end of the week?"""
    hourly_rate = 13.50
    regular_hours_per_day = 8
    overtime_hours_per_day = 2
    workdays_per_week = 5
    regular_weekly_pay = hourly_rate * regular_hours_per_day * workdays_per_week
    overtime_weekly_pay = hourly_rate * overtime_hours_per_day * workdays_per_week
    total_weekly_pay = regular_weekly_pay + overtime_weekly_pay
    result = total_weekly_pay
    return result

print(solution())