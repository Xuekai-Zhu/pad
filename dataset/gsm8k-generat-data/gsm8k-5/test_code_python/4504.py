def solution():
    # Calculate the distance covered in 5 hours of driving
    distance_driven = 8 * 5

    # Calculate the distance covered in 1 hour of cooling down
    distance_cooldown = 0

    # Calculate the distance covered in the remaining 7 hours of driving
    remaining_time = 7
    remaining_distance = 8 * remaining_time

    # Calculate the total distance covered in 13 hours
    total_distance = distance_driven + distance_cooldown + remaining_distance
    result = total_distance
    return result

print(solution())