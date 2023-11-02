def solution():
    """John buys 1/2 gallon jugs of cold brew coffee every 4 days. How many cups of coffee does he drink a day?"""
    # Define the volume of a 1/2 gallon jug in cups
    JUG_VOLUME = 64

    # Define the number of days John takes to consume a 1/2 gallon jug
    JUG_DAYS = 4

    # Calculate the amount of coffee John drinks in cups per day
    cups_per_day = JUG_VOLUME / JUG_DAYS

    result = cups_per_day
    return result

print(solution())