def solution():
    # Define the variables
    num_trips = 10
    mountain_height = 40000
    fraction_covered = 3/4

    # Calculate the distance covered in one round trip
    distance_per_trip = fraction_covered * mountain_height * 2

    # Calculate the total distance covered
    total_distance = num_trips * distance_per_trip
    result = total_distance
    return result

print(solution())