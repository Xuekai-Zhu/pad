def solution():
    """Given a 7-day week, how much does Alex charge for 2 weeks of tutoring if she charges $12 per day?"""
    days_per_week = 7
    weeks = 2
    price_per_day = 12
    total_price = days_per_week * weeks * price_per_day
    result = total_price
    return result

print(solution())