def solution():
    """Before work, Hayden spends 5 minutes ironing his button-up shirt and 3 minutes ironing his pants. He does this 5 days a week. How many minutes does he iron over 4 weeks?"""
    minutes_shirt = 5
    minutes_pants = 3
    days_per_week = 5
    weeks = 4
    total_minutes = (minutes_shirt + minutes_pants) * days_per_week * weeks
    result = total_minutes
    return result

print(solution())