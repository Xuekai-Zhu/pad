def solution():
    """Peter has to walk 2.5 miles to get to the grocery store. If it takes him 20 minutes to walk one mile and he has walked 1 mile already, how many more minutes does he have to walk to reach it?"""
    # Define the distance Peter has to walk
    distance = 2.5 - 1

    # Define the time it takes Peter to walk one mile
    time_per_mile = 20

    # Calculate the total time it will take Peter to walk the remaining distance
    time_remaining = distance * time_per_mile

    # Return the result
    result = time_remaining
    return result

print(solution())