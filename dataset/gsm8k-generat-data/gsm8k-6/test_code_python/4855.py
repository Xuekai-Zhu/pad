def solution():
    # Calculate the total distance driven by Danny
    total_distance = 8 + 8/2 + 3*(8 + 8/2)  # distance to first friend's house + distance to second friend's house + distance from second friend's house to work
    distance_to_work = 3*(8 + 8/2) - 8 - 8/2  # distance from second friend's house to work
    result = distance_to_work
    return result

print(solution())