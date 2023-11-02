def solution():
    """Emberly takes her mornings walks every day. If each walk takes her 1 hour covering 4 miles, and she didn't walk for 4 days in March, calculate the total number of miles she's walked."""
    # Define the distance covered in each walk and the number of walks in March
    DISTANCE_PER_WALK = 4
    WALKS_IN_MARCH = 31 - 4

    # Calculate the total distance covered in March
    total_distance = DISTANCE_PER_WALK * WALKS_IN_MARCH

    # return the result
    result = total_distance
    return result

print(solution())