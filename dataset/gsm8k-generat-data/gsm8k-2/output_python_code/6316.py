def solution():
    """Brady worked 6 hours every day in April. He worked 5 hours every day in June and 8 hours every day in September. What is the average amount of hours that Brady worked per month in those 3 months?"""
    hours_april = 6 * 30
    hours_june = 5 * 30
    hours_september = 8 * 30
    total_hours = hours_april + hours_june + hours_september
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())