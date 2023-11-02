def solution():
    total_time = 8  # Martin was on a business trip for 8 hours
    speed_1 = 70  # Martin's speed during the first half of the trip was 70 km/h
    speed_2 = 85  # Martin's speed during the second half of the trip was 85 km/h

    # Calculate the distance Martin traveled during the first half of the trip
    distance_1 = (speed_1 * total_time) / 2

    # Calculate the distance Martin traveled during the second half of the trip
    distance_2 = (speed_2 * total_time) / 2

    # Calculate the total distance Martin traveled during the whole trip
    total_distance = distance_1 + distance_2
    result = total_distance
    return result

print(solution())