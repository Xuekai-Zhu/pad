def solution():
    """Susan is taking a two week vacation. She works five days a week and has six days of paid vacation. The rest of her workdays will be unpaid vacation time. She gets paid $15 per hour and works 8 hours a day. How much pay will she miss on her vacation?"""
    work_days = 10 # 5 days a week for 2 weeks
    paid_vacation_days = 6
    unpaid_vacation_days = work_days - paid_vacation_days
    daily_pay = 15 * 8 # $15 per hour for 8 hours
    total_unpaid_pay = daily_pay * unpaid_vacation_days
    result = total_unpaid_pay
    return result

print(solution())