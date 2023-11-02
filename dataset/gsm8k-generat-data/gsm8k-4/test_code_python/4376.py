def solution():
    """Austin receives $5 for every hour he helps his father build a deck in their backyard.
    He works for 2 hours on Mondays, an hour on Wednesdays, and 3 hours on Fridays.
    If Austin wants to buy a bicycle that costs $180, how many weeks does he have to work?"""
    # Define the amount Austin earns per week
    weekly_earnings = 5 * (2 + 1 + 3)

    # Calculate the number of weeks required to earn $180
    weeks_required = 180 / weekly_earnings

    # Round up to the nearest whole week
    weeks_required = math.ceil(weeks_required)

    result = weeks_required
    return result

print(solution())