def solution():
    # Convert 30 minutes to 0.5 hours
    time_with_dog = 0.5

    # Calculate the distance covered with the dog
    distance_with_dog = 6 * time_with_dog

    # Convert additional 30 minutes to 0.5 hours
    time_without_dog = 0.5

    # Calculate the distance covered without the dog
    distance_without_dog = 4 * time_without_dog

    # Calculate the total distance covered
    total_distance = distance_with_dog + distance_without_dog
    result = total_distance
    return result

print(solution())