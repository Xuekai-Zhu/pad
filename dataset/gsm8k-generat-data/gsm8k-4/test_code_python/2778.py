def solution():
    """Lexi wants to run a total of three and one-fourth miles. One lap on a particular outdoor track measures a quarter of a mile around. How many complete laps must she run?"""
    # Define the total distance Lexi wants to run
    total_distance = 3.25

    # Define the distance of one lap on the track
    lap_distance = 0.25

    # Calculate the number of complete laps Lexi must run
    laps = total_distance / lap_distance

    # Round the number of laps up to the nearest whole number
    laps = int(round(laps))

    # return the result
    result = laps
    return result

print(solution())