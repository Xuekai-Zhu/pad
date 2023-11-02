def solution():
    """Lexi wants to run a total of three and one-fourth miles. One lap on a particular outdoor track measures a quarter of a mile around. How many complete laps must she run?"""
    # define the total distance in miles
    distance = 3.25

    # define the distance per lap in miles
    lap_distance = 0.25

    # calculate the number of laps needed
    laps = distance / lap_distance

    # round up to the nearest lap
    laps = math.ceil(laps)

    # return the result
    result = laps
    return result

print(solution())