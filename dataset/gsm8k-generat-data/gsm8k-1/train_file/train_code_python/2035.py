def solution():
    """Mr. Johnson has a prescription with enough pills for 30 days. After four-fifths of the days, he has 12 pills left. How many pills is Mr. Johnson supposed to take a day if he takes the same dose daily?"""
    total_days = 30
    remaining_days = total_days - (4/5 * total_days)
    remaining_pills = 12
    pills_per_day = remaining_pills / remaining_days
    result = pills_per_day
    return result

print(solution())