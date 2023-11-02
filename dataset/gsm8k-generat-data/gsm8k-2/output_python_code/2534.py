def solution():
    """Jamie earns $10 an hour by delivering flyers. She delivers flyers 2 days each week. It takes her 3 hours each time she delivers flyers. After delivering flyers for 6 weeks, how much money will she have earned?"""
    hourly_rate = 10
    delivery_days_per_week = 2
    delivery_hours_per_day = 3
    delivery_hours_per_week = delivery_days_per_week * delivery_hours_per_day
    weeks_delivering = 6
    total_delivery_hours = weeks_delivering * delivery_hours_per_week
    total_earned = hourly_rate * total_delivery_hours
    result = total_earned
    return result

print(solution())