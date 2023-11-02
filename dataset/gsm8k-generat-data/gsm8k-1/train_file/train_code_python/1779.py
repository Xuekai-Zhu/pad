def solution():
    """Faith is getting paid $13.50 per hour. She normally works 8 hours a day, 5 days a week, plus 2 hours of overtime per day. How much will she earn by the end of the week?"""
    hourly_rate = 13.50
    regular_hours_per_day = 8
    overtime_hours_per_day = 2
    days_per_week = 5
    regular_hours_per_week = regular_hours_per_day * days_per_week
    overtime_hours_per_week = overtime_hours_per_day * days_per_week
    total_hours_per_week = regular_hours_per_week + overtime_hours_per_week
    total_earnings = total_hours_per_week * hourly_rate
    result = total_earnings
    return result

print(solution())