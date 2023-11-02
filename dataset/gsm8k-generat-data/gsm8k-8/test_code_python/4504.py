def solution():
    # Define the car's speed in miles per hour
    speed = 8

    # Calculate the distance the car can drive in 5 hours
    distance_before_cooling = speed * 5

    # Calculate the distance the car can drive in the remaining 8 hours
    distance_after_cooling = speed * 8

    # Calculate the total distance the car can drive in 13 hours
    total_distance = distance_before_cooling + distance_after_cooling
    result = total_distance
    return result

print(solution())