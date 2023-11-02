def solution():
    """Rick took off on a road trip for the summer. He traveled to the first destination on his trip, and then from there, he traveled twice the distance to this second destination. The third point on his trip was 40 miles away, which was half the distance he traveled from the beginning to his first destination. The final destination took twice the amount of driving of all the other legs put together. How many miles in total did he travel across all the legs of the trip?"""
    # Define the distances of the legs of the trip
    distance_1 = None
    distance_2 = None
    distance_3 = 40
    distance_4 = None

    # Calculate the distance of the first leg
    distance_1 = distance_3 * 2

    # Calculate the distance of the second leg
    distance_2 = distance_1 * 2

    # Calculate the distance of the last leg
    distance_4 = (distance_1 + distance_2 + distance_3) * 2

    # Calculate the total distance of the trip
    total_distance = distance_1 + distance_2 + distance_3 + distance_4

    # return the result
    result = total_distance
    return result

print(solution())