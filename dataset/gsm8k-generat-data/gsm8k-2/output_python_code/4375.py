def solution():
    """Austin receives $5 for every hour he helps his father build a deck in their backyard. He works for 2 hours on Mondays, an hour on Wednesdays, and 3 hours on Fridays. If Austin wants to buy a bicycle that costs $180, how many weeks does he have to work?"""
    hours_per_week = 2 + 1 + 3
    wage_per_week = hours_per_week * 5
    weeks_to_buy_bike = 180 / wage_per_week
    result = weeks_to_buy_bike
    return result

print(solution())