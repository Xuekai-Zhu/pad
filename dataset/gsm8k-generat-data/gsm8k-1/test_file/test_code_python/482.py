def solution():
    """James runs 12 miles a day for 5 days a week. If he runs 10 miles an hour how many hours does he run a week?"""
    miles_per_day = 12
    days_per_week = 5
    miles_per_hour = 10
    hours_per_week = (miles_per_day * days_per_week) / miles_per_hour
    result = hours_per_week
    return result

print(solution())