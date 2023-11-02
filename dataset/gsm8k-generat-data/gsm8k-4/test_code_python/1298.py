def solution():
    """An airplane took a trip along the Eastern Coast of the USA. During the trip, the plane hovered in Mountain time for 3 hours, Central time for 4 hrs, and Eastern time for 2 hrs. The next day it took 2 more hours to hover in each of the places it passed through the previous day. Calculate the total time it took the plane to hover over Mountain time, Central time, and Eastern time in the two days."""
    # Define the initial hours of hovering in each time zone
    mountain_time = 3
    central_time = 4
    eastern_time = 2

    # Define the additional hours of hovering in each time zone on the next day
    additional_hours = 2

    # Calculate the total hours of hovering in each time zone during the two days
    mountain_total = mountain_time + additional_hours
    central_total = central_time + additional_hours
    eastern_total = eastern_time + additional_hours

    # Calculate the overall total hours of hovering
    total_hours = mountain_total + central_total + eastern_total

    # return the result
    result = total_hours
    return result

print(solution())