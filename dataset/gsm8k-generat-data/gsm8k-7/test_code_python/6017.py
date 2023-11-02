def solution():
    num_trips = 10
    mountain_height = 40000
    fraction_of_height_reached = 3 / 4

    # Calculate the distance covered in one round trip
    one_trip_distance = 2 * fraction_of_height_reached * mountain_height

    # Calculate the total distance covered in all round trips
    total_distance = num_trips * one_trip_distance
    result = total_distance
    return result

print(solution())