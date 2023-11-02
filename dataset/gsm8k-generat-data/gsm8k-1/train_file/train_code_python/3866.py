def solution():
    """Susan is taking a two week vacation. She works five days a week and has six days of paid vacation. The rest of her workdays will be unpaid vacation time. She gets paid $15 per hour and works 8 hours a day. How much pay will she miss on her vacation?"""
    work_days_per_week = 5
    paid_vacation_days = 6
    unpaid_vacation_days = 4
    hours_per_day = 8
    pay_per_hour = 15
    total_work_days = work_days_per_week * 2 - paid_vacation_days + unpaid_vacation_days
    total_hours = total_work_days * hours_per_day
    total_pay_missed = total_hours * pay_per_hour
    result = total_pay_missed
    
    return result

print(solution())