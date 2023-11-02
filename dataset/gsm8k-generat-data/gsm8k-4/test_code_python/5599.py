def solution():
    """When doing her exercises, Mairead runs for 40 miles, walks for 3/5 times as many miles as she ran, and walks for five times the number of miles she jogged. Calculate the total distance Mairead has covered while doing her exercises."""
    # Define the distance Mairead ran
    distance_run = 40

    # Calculate the distance Mairead walked
    distance_walked = (3/5) * distance_run

    # Calculate the distance Mairead jogged
    distance_jogged = distance_walked / 5

    # Calculate the total distance Mairead covered
    total_distance = distance_run + distance_walked + distance_jogged

    # return the result
    result = total_distance
    return result

print(solution())