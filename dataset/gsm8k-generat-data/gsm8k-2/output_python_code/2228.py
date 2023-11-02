def solution():
    """Zainab earns $2 an hour passing out flyers at the town square. She passes out flyers on Monday, Wednesday, and Saturday each week, for 4 hours at a time. After passing out flyers for 4 weeks, how much money will Zainab earn?"""
    hourly_rate = 2
    hours_per_day = 4
    days_per_week = 3
    weeks = 4
    total_hours = hours_per_day * days_per_week * weeks
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())