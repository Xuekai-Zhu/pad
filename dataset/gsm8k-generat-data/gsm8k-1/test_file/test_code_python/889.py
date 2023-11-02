def solution():
    """Mark works at his job for 8 hours a day for 5 days a week. He used to make $10 an hour but they raised his pay by $2 per hour. How much does he make a week?"""
    hours_per_day = 8
    days_per_week = 5
    old_pay_rate = 10
    pay_raise = 2
    new_pay_rate = old_pay_rate + pay_raise
    weekly_pay = hours_per_day * new_pay_rate * days_per_week
    result = weekly_pay
    return result

print(solution())