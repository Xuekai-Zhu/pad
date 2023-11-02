def solution():
    # Define the distances
    distance_to_friend1 = 8
    distance_to_friend2 = distance_to_friend1 / 2
    total_distance_to_work = distance_to_friend1 + distance_to_friend2 + (3 * (distance_to_friend1 + distance_to_friend2))

    # Calculate the distance Danny drives between the second friend's house and work
    distance_to_work_from_friend2 = total_distance_to_work - (distance_to_friend1 + distance_to_friend2)
    result = distance_to_work_from_friend2
    return result

print(solution())