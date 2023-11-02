def solution():
    # Calculate the total distance of the first two walks
    total_distance = 20 + 200

    # Calculate the distance of the third walk
    third_walk = total_distance * 2

    # Calculate the distance of the fourth walk
    fourth_walk = (total_distance + third_walk) / 2

    # Calculate the total distance of the whole trip
    total_trip_distance = 2 * (total_distance + third_walk + fourth_walk)

    result = total_trip_distance
    return result

print(solution())