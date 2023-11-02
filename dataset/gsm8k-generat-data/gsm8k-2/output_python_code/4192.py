def solution():
    """Before work, Hayden spends 5 minutes ironing his button-up shirt and 3 minutes ironing his pants. He does this 5 days a week. How many minutes does he iron over 4 weeks?"""
    shirt_time = 5
    pant_time = 3
    days_per_week = 5
    weeks = 4
    total_time = (shirt_time + pant_time) * days_per_week * weeks
    result = total_time
    return result

print(solution())