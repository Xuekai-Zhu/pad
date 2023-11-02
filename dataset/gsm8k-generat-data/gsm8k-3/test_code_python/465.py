def solution():
    """A man is returning home from work and trying to decide which route to take.  His first route option includes 3 stoplights.  This route will take him 10 minutes if all three lights are green, but each light that is red will add 3 minutes to the trip.  The second route does not include any stoplights and takes 14 minutes.  If the man chooses the first route, how much longer will his trip be if all 3 stoplights are red?"""
    # Define the time it takes to travel each route with no red lights
    ROUTE1_TIME = 10
    ROUTE2_TIME = 14

    # Calculate the time it takes to travel route 1 with all 3 lights red
    route1_red_time = ROUTE1_TIME + 3*3

    # Calculate the difference in time between route 1 with all red lights and route 2
    time_diff = route1_red_time - ROUTE2_TIME

    # Display the time difference
    result = time_diff
    return result

print(solution())