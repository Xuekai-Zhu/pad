def solution():
    """Brady worked 6 hours every day in April. He worked 5 hours every day in June and 8 hours every day in September. What is the average amount of hours that Brady worked per month in those 3 months?"""
    days_in_april = 30
    days_in_june = 30
    days_in_sept = 30
    hours_in_april = 6
    hours_in_june = 5
    hours_in_sept = 8
    total_hours = (days_in_april * hours_in_april) + (days_in_june * hours_in_june) + (days_in_sept * hours_in_sept)
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())