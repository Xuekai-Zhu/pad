def solution():
    """Maddy was given 40 chocolate eggs for Easter. She likes to eat two each day after school. If Maddy has two chocolate eggs after school each day, how many weeks will they last?"""
    eggs_per_day = 2
    days_per_week = 7
    total_days = 40 / eggs_per_day
    weeks = total_days / days_per_week
    result = weeks
    return result

print(solution())