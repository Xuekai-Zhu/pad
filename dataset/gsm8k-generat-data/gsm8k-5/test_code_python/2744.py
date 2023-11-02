def solution():
    distance_potato = 6 * 200 * 3  # Distance in yards that the potato can be launched
    distance_dog = 400  # Distance the dog can run in feet per minute

    # Calculate the time it takes the dog to fetch the potato
    time_fetch = (distance_potato / (distance_dog / 60))
    result = time_fetch
    return result

print(solution())