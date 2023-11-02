def solution():
    """An airplane took a trip along the Eastern Coast of the USA. During the trip, the plane hovered in Mountain time for 3 hours, Central time for 4 hrs, and Eastern time for 2 hrs. The next day it took 2 more hours to hover in each of the places it passed through the previous day. Calculate the total time it took the plane to hover over Mountain time, Central time, and Eastern time in the two days."""
    # Define the initial hours of hovering in each time zone
    MOUNTAIN_TIME = 3
    CENTRAL_TIME = 4
    EASTERN_TIME = 2

    # Define the additional hours of hovering in each time zone the next day
    ADDITIONAL_HOURS = 2

    # Calculate the total hours of hovering in each time zone over the two days
    total_mountain_time = MOUNTAIN_TIME + ADDITIONAL_HOURS
    total_central_time = CENTRAL_TIME + ADDITIONAL_HOURS
    total_eastern_time = EASTERN_TIME + ADDITIONAL_HOURS

    # Calculate the total time of hovering over all time zones
    total_time = total_mountain_time + total_central_time + total_eastern_time

    # Display the total time of hovering over all time zones
    result = total_time
    return result

print(solution())