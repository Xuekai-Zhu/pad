def solution():
    """An airplane took a trip along the Eastern Coast of the USA. During the trip, the plane hovered in Mountain time for 3 hours, Central time for 4 hrs, and Eastern time for 2 hrs. The next day it took 2 more hours to hover in each of the places it passed through the previous day. Calculate the total time it took the plane to hover over Mountain time, Central time, and Eastern time in the two days."""
    mountain_hours = 3 + 2
    central_hours = 4 + 2
    eastern_hours = 2 + 2
    total_hours = mountain_hours + central_hours + eastern_hours
    result = total_hours
    return result

print(solution())