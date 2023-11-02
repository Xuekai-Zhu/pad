def solution():
    """Liz roasts 2 16 pounds turkeys every Thanksgiving.  She can only roast them 1 at a time because she has a small oven.  She roasts each turkey for 15 minutes per pound.  If dinner is served at 6:00 pm what is the latest time she can start roasting the turkeys?"""
    # Define the weight of each turkey and the time required to roast each pound
    TURKEY_WEIGHT = 16
    TIME_PER_POUND = 15  # in minutes

    # Calculate the total time required to roast both turkeys
    total_time = TURKEY_WEIGHT * 2 * TIME_PER_POUND

    # Calculate the time she needs to start roasting the turkeys
    dinner_time = datetime.datetime(2021, 11, 25, 18, 0)  # Thanksgiving dinner is served at 6:00 pm
    start_time = dinner_time - datetime.timedelta(minutes=total_time)

    result = str(start_time.time())
    return result

print(solution())