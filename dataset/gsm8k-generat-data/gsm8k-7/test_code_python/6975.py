def solution():
    distance_1 = 3  # km
    time_1 = 2  # hours
    distance_2 = 12  # km

    # Calculate the speed of Ben in km/hour
    speed = distance_1 / time_1

    # Calculate the time it would take him to travel 12 km
    time_2 = distance_2 / speed

    # Convert the time to minutes
    time_2_minutes = time_2 * 60
    result = time_2_minutes
    return result

print(solution())