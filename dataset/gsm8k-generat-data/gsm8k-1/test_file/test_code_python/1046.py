def solution():
    """It is approximately 1955 kilometers from San Diego, California to New York City, New York. If Bernice drove 325 kilometers for 4 days, how many kilometers will she still need to drive?"""
    total_distance = 1955
    distance_driven = 325 * 4
    distance_left = total_distance - distance_driven
    result = distance_left
    return result

print(solution())