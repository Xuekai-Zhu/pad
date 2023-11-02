def solution():
    total_distance = 18
    afternoon_distance = 2 * morning_distance  # Let morning_distance be x
    bike_distance = 12

    # Calculate the total distance traveled without the morning run
    other_distance = afternoon_distance + bike_distance

    # Calculate the morning run distance
    morning_distance = total_distance - other_distance
    result = morning_distance
    return result

print(solution())