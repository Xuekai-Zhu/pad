def solution():
    # Calculate the total distance covered in the first 3 hours
    distance_covered_first_3_hours = 50 * 3

    # Calculate the total distance covered in the next 4 hours
    distance_covered_next_4_hours = 80 * 4

    # Calculate the total distance covered so far
    total_distance_covered = distance_covered_first_3_hours + distance_covered_next_4_hours

    # Calculate the remaining distance to the hotel
    remaining_distance = 600 - total_distance_covered
    result = remaining_distance
    return result

print(solution())