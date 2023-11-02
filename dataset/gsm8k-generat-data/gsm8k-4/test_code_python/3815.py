def solution():
    """Richard starts walking from Cincinnati to New York City, which is 70 miles. Richards walks 20 miles the first day. The next day he walks 6 miles less than half as much as he walked the first day. He walks 10 miles the third day. How many miles further does Richard have to walk to be in New York City?"""
    # Define the total distance to New York City
    total_distance = 70

    # Calculate the distance Richard has walked so far
    distance_walked = 20 + ((1/2) * 20) - 6 + 10

    # Calculate the distance left to walk
    distance_left = total_distance - distance_walked

    # return the result
    result = distance_left
    return result

print(solution())