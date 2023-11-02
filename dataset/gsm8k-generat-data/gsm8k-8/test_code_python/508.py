def solution():
    # Calculate the distance covered in the first half hour
    dist_first_half = 30 * 0.5

    # Calculate the time and speed for the second half of the trip
    time_second_half = 0.5 * 2
    speed_second_half = 2 * 30

    # Calculate the distance covered in the second half of the trip
    dist_second_half = speed_second_half * time_second_half

    # Calculate the total distance covered
    total_dist = dist_first_half + dist_second_half
    result = total_dist
    return result

print(solution())