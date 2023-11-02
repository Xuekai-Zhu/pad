def solution():
    """Percy swims 1 hour before school and 1 after school 5 days a week. He swims 3 hours on the weekend. How many hours of swimming does he do over 4 weeks?"""
    daily_swim_hours = 2
    weekend_swim_hours = 3
    weeks = 4
    total_swim_hours = (daily_swim_hours * 5 + weekend_swim_hours) * weeks
    result = total_swim_hours
    return result

print(solution())