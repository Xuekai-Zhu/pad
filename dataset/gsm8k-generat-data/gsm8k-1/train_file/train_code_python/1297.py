def solution():
    """An airplane took a trip along the Eastern Coast of the USA. During the trip, the plane hovered in Mountain time for 3 hours, Central time for 4 hrs, and Eastern time for 2 hrs. The next day it took 2 more hours to hover in each of the places it passed through the previous day. Calculate the total time it took the plane to hover over Mountain time, Central time, and Eastern time in the two days."""
    day_one = 3 + 4 + 2  # total hours spent on day one
    day_two = (3 + 2) + (4 + 2) + (2 + 2)  # total hours spent on day two
    total_time = day_one + day_two  # total time over two days
    result = total_time
    return result

print(solution())