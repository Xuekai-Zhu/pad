def solution():
    # Calculate the distance driven at 28 mph
    distance_at_28 = 14 * (28/60)

    # Calculate the distance driven at 60 mph
    distance_at_60 = 14 * (60/60)

    # Calculate the total distance
    total_distance = distance_at_28 + distance_at_60

    # Calculate Jake's biking time
    jake_biking_time = total_distance / 11

    result = jake_biking_time
    return result

print(solution())