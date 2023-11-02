def solution():
    """Stan hires a magician for $60 an hour. He works 3 hours every day for 2 weeks. How much money does he pay the magician?"""
    hourly_rate = 60
    hours_per_day = 3
    days_per_week = 7
    weeks = 2
    total_hours = hours_per_day * days_per_week * weeks
    total_cost = total_hours * hourly_rate
    result = total_cost
    return result

print(solution())