def solution():
    """Liz roasts 2 16 pounds turkeys every Thanksgiving.  She can only roast them 1 at a time because she has a small oven.  She roasts each turkey for 15 minutes per pound.  If dinner is served at 6:00 pm what is the latest time she can start roasting the turkeys?"""
    # Define the weight of each turkey and the time needed to roast each pound
    TURKEY_WEIGHT = 16
    ROASTING_TIME_PER_POUND = 15

    # Calculate the total roasting time for both turkeys
    total_time = TURKEY_WEIGHT * ROASTING_TIME_PER_POUND * 2

    # Convert the total roasting time to hours and minutes
    hours = total_time // 60
    minutes = total_time % 60

    # Calculate the time Liz needs to start roasting
    latest_start_time = datetime.datetime(2021, 11, 25, 18, 0) - datetime.timedelta(hours=hours, minutes=minutes)

    # Display the latest start time
    result = latest_start_time.time()
    return result

print(solution())