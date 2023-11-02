def solution():
    """Peter has to walk 2.5 miles to get to the grocery store. If it takes him 20 minutes to walk one mile and he has walked 1 mile already, how many more minutes does he have to walk to reach it?"""
    # Define the distance Peter has left to walk
    distance_left = 2.5 - 1

    # Calculate the time it will take Peter to walk the remaining distance
    time_left = distance_left * 20

    # Display the time Peter has left to walk
    result = time_left
    return result

print(solution())