def solution():
    """Jamie earns $10 an hour by delivering flyers. She delivers flyers 2 days each week. It takes her 3 hours each time she delivers flyers. After delivering flyers for 6 weeks, how much money will she have earned?"""
    hourly_rate = 10
    days_per_week = 2
    hours_per_day = 3
    weeks_delivering = 6
    total_hours = days_per_week * hours_per_day * weeks_delivering
    total_money_earned = total_hours * hourly_rate
    result = total_money_earned
    return result

print(solution())