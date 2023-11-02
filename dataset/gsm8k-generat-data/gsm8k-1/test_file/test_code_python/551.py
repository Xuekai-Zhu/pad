def solution():
    """John plans to save money from working. He gets paid $2 per hour and works 5 hours a day for 4 days a week. If he wants to save $80 how many weeks will it take him?"""
    pay_per_hour = 2
    hours_per_day = 5
    days_per_week = 4
    weekly_earnings = pay_per_hour * hours_per_day * days_per_week
    weeks_to_save = 80 / weekly_earnings
    result = weeks_to_save
    return result

print(solution())