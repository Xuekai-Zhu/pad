def solution():
    """The city’s bus system carries 1,200,000 people each day. How many people does the bus system carry for 13 weeks?"""
    daily_ridership = 1200000
    days_per_week = 7
    total_ridership = daily_ridership * days_per_week * 13
    result = total_ridership
    return result

print(solution())