def solution():
    """Jim spends 2 hours watching TV and then decides to go to bed and reads for half as long. He does this 3 times a week. How many hours does he spend on TV and reading in 4 weeks?"""
    tv_hours = 2
    reading_hours = tv_hours / 2
    days_per_week = 3
    total_hours_per_week = tv_hours + reading_hours
    total_hours_per_month = total_hours_per_week * 4
    total_hours = total_hours_per_month * days_per_week
    result = total_hours
    return result

print(solution())