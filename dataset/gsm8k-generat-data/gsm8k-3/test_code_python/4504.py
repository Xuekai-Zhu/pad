def solution():
    """An old car can drive 8 miles in one hour. After 5 hours of constant driving, the car needs to get cooled down which takes 1 hour. How many miles can this car drive in 13 hours?"""
    # Define the car's speed
    SPEED = 8

    # Calculate the distance driven in the first 5 hours
    distance_first_5 = SPEED * 5

    # Calculate the distance driven after the cooling down period
    distance_after_cooling = SPEED * 1

    # Calculate the distance driven in the remaining 7 hours
    distance_last_7 = SPEED * 7

    # Calculate the total distance driven
    total_distance = distance_first_5 + distance_after_cooling + distance_last_7

    # Display the total distance driven
    result = total_distance
    return result

print(solution())