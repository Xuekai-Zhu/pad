def solution():
    # Calculate the distance covered in the first 4.5 hours
    distance_1 = 20 * 4.5

    # Calculate the distance covered when going uphill for 2.5 hours
    distance_2 = 12 * 2.5

    # Calculate the distance covered when going downhill for 1.5 hours
    distance_3 = 24 * 1.5

    # Calculate the total distance covered before puncturing the tire
    total_distance = distance_1 + distance_2 + distance_3

    # Calculate the distance Alex had to walk
    distance_walked = 164 - total_distance
    result = distance_walked
    return result

print(solution())