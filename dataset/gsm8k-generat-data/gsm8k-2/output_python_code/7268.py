def solution():
    """Stan hires a magician for $60 an hour. He works 3 hours every day for 2 weeks. How much money does he pay the magician?"""
    hourly_rate = 60
    daily_hours = 3
    num_of_days = 14 # two weeks
    total_hours = daily_hours * num_of_days
    total_cost = total_hours * hourly_rate
    result = total_cost
    return result

print(solution())