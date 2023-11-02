def solution():
    launch_distance = 6 * 200 * 3  # distance in feet
    dog_speed = 400  # feet per minute

    # Calculate the time it takes for the dog to retrieve the potato
    time = launch_distance / dog_speed

    result = time
    return result

print(solution())