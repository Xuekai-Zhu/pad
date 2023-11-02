def solution():
    # Define the distance and walking speed
    distance = 2.5
    speed = 20  # minutes per mile

    # Calculate how many minutes it will take to walk the remaining distance
    remaining_distance = distance - 1  # since Peter has already walked 1 mile
    remaining_time = remaining_distance * speed

    result = remaining_time
    return result

print(solution())