def solution():
    """An old car can drive 8 miles in one hour. After 5 hours of constant driving, the car needs to get cooled down which takes 1 hour. How many miles can this car drive in 13 hours?"""
    driving_speed = 8
    driving_time = 5
    cooldown_time = 1
    total_driving_time = 13

    # Calculate distance driven during constant driving time
    distance_driven = driving_speed * driving_time

    # Calculate remaining driving time after cooldown
    remaining_time = total_driving_time - driving_time - cooldown_time

    # Calculate total distance driven
    total_distance = distance_driven + (remaining_time * driving_speed)

    result = total_distance
    return result

print(solution())