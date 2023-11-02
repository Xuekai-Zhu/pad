def solution():
    """Tim does 100 tasks a day. They each pay $1.2. If he works 6 days a week how much does he make a week?"""
    tasks_per_day = 100
    pay_per_task = 1.2
    days_per_week = 6
    weekly_income = tasks_per_day * pay_per_task * days_per_week
    result = weekly_income
    return result

print(solution())