def solution():
    """Austin receives $5 for every hour he helps his father build a deck in their backyard. He works for 2 hours on Mondays, an hour on Wednesdays, and 3 hours on Fridays. If Austin wants to buy a bicycle that costs $180, how many weeks does he have to work?"""
    # Define the amount Austin earns per hour
    HOURLY_RATE = 5

    # Define the number of hours Austin works each week
    hours_per_week = 2 + 1 + 3

    # Define the cost of the bicycle
    bicycle_cost = 180

    # Calculate the number of weeks Austin needs to work
    weeks_to_work = bicycle_cost / (HOURLY_RATE * hours_per_week)

    # Display the number of weeks
    result = weeks_to_work
    return result

print(solution())