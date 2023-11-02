def solution():
    """The city’s bus system carries 1,200,000 people each day. How many people does the bus system carry for 13 weeks?"""
    people_per_day = 1200000
    days_per_week = 7
    weeks = 13
    total_people = people_per_day * days_per_week * weeks
    result = total_people
    return result

print(solution())