def solution():
    """Mr. Johnson has a prescription with enough pills for 30 days. After four-fifths of the days, he has 12 pills left. How many pills is Mr. Johnson supposed to take a day if he takes the same dose daily?"""
    total_days = 30
    days_left = total_days - (4/5 * total_days)
    pills_left = 12
    pills_per_day = (total_days * pills_left) / days_left
    result = pills_per_day
    return result

print(solution())